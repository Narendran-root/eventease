# middleware.py
import logging
from datetime import datetime

logger = logging.getLogger("bookings")
handler = logging.FileHandler("bookings.log")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def log_booking(user_id, event_id):
    logger.info(f"Booking by user={user_id}, event={event_id}, time={datetime.utcnow()}")
