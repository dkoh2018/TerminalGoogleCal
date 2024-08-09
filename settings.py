from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from openai import OpenAI


def calendar_settings():
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

    time_min = datetime.now() - timedelta(days=0)
    time_max = datetime.now() + timedelta(days=10)

    events = gc.get_events(time_min, time_max, order_by="startTime", single_events=True)

    for event in events:
        print(event)


if __name__ == "__main__":
    calendar_settings()
