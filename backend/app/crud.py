# crud.py
from app import models
from fastapi import HTTPException
from sqlalchemy import select, func
from datetime import datetime
import random, string

async def create_booking(db, user_id: int, event_id: int):
    # Check if user already booked
    existing = await db.fetch_one(
        models.bookings.select().where(
            (models.bookings.c.user_id == user_id) &
            (models.bookings.c.event_id == event_id)
        )
    )
    if existing:
        raise HTTPException(status_code=400, detail="User already booked this event")

    # Check event capacity
    event = await db.fetch_one(models.events.select().where(models.events.c.id == event_id))
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Count current bookings for the event
    count_query = select(func.count()).select_from(models.bookings).where(models.bookings.c.event_id == event_id)
    booked_count = await db.fetch_val(count_query)

    if booked_count >= event.capacity:
        raise HTTPException(status_code=400, detail="Event full")

    # Generate booking ID
    rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    booking_id = f"BKG-{datetime.today().strftime('%b').upper()}{datetime.today().year}-{rand_str}"

    # Insert booking
    await db.execute(
        models.bookings.insert().values(
            booking_id=booking_id,
            user_id=user_id,
            event_id=event_id,
            created_at=datetime.utcnow()
        )
    )

    return booking_id
