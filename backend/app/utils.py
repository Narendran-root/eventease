# utils.py
import random, string
from datetime import datetime

def generate_booking_id():
    now = datetime.utcnow()
    mmm = now.strftime("%b").upper()   # e.g., SEP
    yyyy = now.strftime("%Y")          # e.g., 2025
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return f"BKG-{mmm}{yyyy}-{rand}"
