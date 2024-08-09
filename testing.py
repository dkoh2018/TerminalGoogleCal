from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os

# Load environment variables from .env.local
load_dotenv(dotenv_path=".env.local")

# Retrieve the variables
credentials_path = os.getenv("CREDENTIALS_PATH")
token_path = os.getenv("TOKEN_PATH")

# Initialize GoogleCalendar with the environment variables
gc = GoogleCalendar(
    credentials_path=credentials_path,
    token_path=token_path,
)

# Get and print settings
settings = gc.get_settings()
print(f"\n{settings}")
