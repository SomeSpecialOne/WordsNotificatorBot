import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TEST")
admin = os.getenv("admin_id")
