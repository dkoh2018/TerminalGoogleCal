from gcsa.google_calendar import GoogleCalendar
import os
from dotenv import load_dotenv


def calendar_settings():
    load_dotenv(dotenv_path=".env.local")

    # Retrieve the variables
    credentials_path = os.getenv("CREDENTIALS_PATH")
    token_path = os.getenv("TOKEN_PATH")

    # Initialize GoogleCalendar with the environment variables
    gc = GoogleCalendar(
        credentials_path=credentials_path,
        token_path=token_path,
    )

    settings = gc.get_settings()
    print(f"\n{settings}")
    print("\n...is there anything else you'd like to do?\n")


if __name__ == "__main__":
    calendar_settings()
