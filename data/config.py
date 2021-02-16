import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("WORD_N")
admin = os.getenv("admin_id")
