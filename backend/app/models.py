from sqlalchemy import Table, Column, Integer, String, Text, Date, DateTime, ForeignKey, func, MetaData
from sqlalchemy.sql import text

metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(255), unique=True, nullable=False),
    Column("password_hash", Text, nullable=False),
    Column("full_name", String(255)),
    Column("role", String(20), default="user"),
    Column("created_at", DateTime, server_default=func.now()),
)

events = Table(
    "events", metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255), nullable=False),
    Column("description", Text),
    Column("location", String(255)),
    Column("category", String(100)),
    Column("date", Date, nullable=False),
    Column("capacity", Integer, nullable=False, default=0),
    Column("created_at", DateTime, server_default=func.now()),
)

bookings = Table(
    "bookings", metadata,
    Column("id", Integer, primary_key=True),
    Column("booking_id", String(50), unique=True, nullable=False),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("event_id", Integer, ForeignKey("events.id", ondelete="CASCADE")),
    Column("created_at", DateTime, server_default=func.now()),
)
