from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from datetime import date, datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: Annotated[str, Field(min_length=6, max_length=72)]
    full_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class EventCreate(BaseModel):
    title: str
    description: str
    location: str
    category: str
    date: date
    capacity: int

class EventOut(BaseModel):
    id: int
    title: str
    location: str
    date: date
    description: str
    category: str
    capacity: int

class BookingOut(BaseModel):
    booking_id: str
    event_id: int
    user_id: int
    created_at: datetime
