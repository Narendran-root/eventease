import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Depends, HTTPException, status
from databases import Database
from datetime import date
from fastapi.middleware.cors import CORSMiddleware

from app import models, schemas, auth, crud, middleware
from app.dependencies import get_current_user
from app.config import DATABASE_URL
from app.auth import get_password_hash
from app.schemas import UserCreate


app = FastAPI(title="EventEase API")

# Add CORS middleware here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev, or ["http://localhost:8080"] for Flutter web
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


# ✅ USER REGISTRATION
@app.post("/register")
async def register_user(user: UserCreate):
    # Check if user already exists
    existing = await db.fetch_one(
        models.users.select().where(models.users.c.email == user.email)
    )
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)

    query = models.users.insert().values(
        email=user.email,
        full_name=user.full_name,
        password_hash=hashed_password,
        role="user"  # default role
    )
    await db.execute(query)

    return {"message": "User registered successfully"}

# ✅ USER LOGIN
@app.post("/login")
async def login(user: schemas.UserLogin):
    record = await db.fetch_one(models.users.select().where(models.users.c.email == user.email))

    if not record:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Verify password
    if not auth.verify_password(user.password, record.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Generate JWT token
    token = auth.create_access_token({
        "id": record.id,
        "email": record.email,
        "role": record.role
    })
    return {"access_token": token, "token_type": "bearer"}


# ✅ GET ALL EVENTS
@app.get("/events")
async def list_events():
    return await db.fetch_all(models.events.select())


# ✅ ADMIN CREATE EVENT
@app.post("/admin/events")
async def create_event(event: schemas.EventCreate, current_user=Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(403, "Admin only")
    query = models.events.insert().values(**event.dict())
    await db.execute(query)
    return {"message": "Event created"}


# ✅ BOOK EVENT
@app.post("/events/{event_id}/book")
async def book_event(event_id: int, current_user=Depends(get_current_user)):
    booking_id = await crud.create_booking(db, current_user["id"], event_id)
    middleware.log_booking(current_user["id"], event_id)
    return {"booking_id": booking_id}


# ✅ VIEW MY BOOKINGS
@app.get("/bookings")
async def my_bookings(current_user=Depends(get_current_user)):
    q = models.bookings.select().where(models.bookings.c.user_id == current_user["id"])
    return await db.fetch_all(q)


# ✅ CANCEL BOOKING
@app.delete("/bookings/{booking_id}")
async def cancel_booking(booking_id: str, current_user=Depends(get_current_user)):
    b = await db.fetch_one(models.bookings.select().where(models.bookings.c.booking_id == booking_id))
    if not b:
        raise HTTPException(404, "Booking not found")

    event = await db.fetch_one(models.events.select().where(models.events.c.id == b.event_id))
    if event.date <= date.today():
        raise HTTPException(400, "Cannot cancel event already started")

    await db.execute(models.bookings.delete().where(models.bookings.c.booking_id == booking_id))
    return {"status": "cancelled"}
