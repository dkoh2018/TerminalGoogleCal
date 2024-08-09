from gcsa.google_calendar import GoogleCalendar
import os
from dotenv import load_dotenv


def delete_an_event():
    # initialize GoogleCalendar with the environment variables
    load_dotenv(dotenv_path=".env.local")

    credentials_path = os.getenv("CREDENTIALS_PATH")
    token_path = os.getenv("TOKEN_PATH")

    gc = GoogleCalendar(
        credentials_path=credentials_path,
        token_path=token_path,
    )

    print("View events functionality to be implemented.")
    # TODO: Implement event viewing logic
    # 1. Fetch upcoming events
    # 2. Display events in a user-friendly format


if __name__ == "__main__":
    delete_an_event()
