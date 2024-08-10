from gcsa.google_calendar import GoogleCalendar
import os
from dotenv import load_dotenv
from authenticate_calendar import authenticate_calendar


def calendar_settings():
    gc = authenticate_calendar()

    settings = gc.get_settings()
    print(f"\n{settings}")
    print("\n...is there anything else you'd like to do?\n")


if __name__ == "__main__":
    calendar_settings()
