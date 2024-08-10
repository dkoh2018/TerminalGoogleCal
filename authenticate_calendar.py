from gcsa.google_calendar import GoogleCalendar
import os
from dotenv import load_dotenv


def authenticate_calendar():
    load_dotenv(dotenv_path=".env.local")

    credentials_path = os.getenv("CREDENTIALS_PATH")
    token_path = os.getenv("TOKEN_PATH")

    gc = GoogleCalendar(
        credentials_path=credentials_path,
        token_path=token_path,
    )
    return gc
