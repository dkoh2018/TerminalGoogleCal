from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta


def view_events():
    load_dotenv(dotenv_path=".env.local")

    credentials_path = os.getenv("CREDENTIALS_PATH")
    token_path = os.getenv("TOKEN_PATH")

    gc = GoogleCalendar(
        credentials_path=credentials_path,
        token_path=token_path,
    )

    # prompt the user to select a time range
    print("\nselect a time range option:\n")
    print("  1) next 2 weeks from today")
    print("  2) past 2 weeks from today")
    print("  3) past week and this week\n")
    choice = input("enter the option number (1/2/3): ")

    if choice == "1":
        time_min = datetime.now() - timedelta(days=0)
        time_max = datetime.now() + timedelta(days=14)
    elif choice == "2":
        time_min = datetime.now() - timedelta(days=14)
        time_max = datetime.now() + timedelta(days=0)
    elif choice == "3":
        time_min = datetime.now() - timedelta(days=7)
        time_max = datetime.now() + timedelta(days=7)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    events = list(
        gc.get_events(time_min, time_max, order_by="startTime", single_events=True)
    )

    # print each event with a border around it
    max_len = max(len(str(event)) for event in events)

    for event in events:
        event_str = str(event)
        print("+" + "-" * (max_len + 2) + "+")
        print(f"| {event_str} ".ljust(max_len + 3) + "|")
        print("+" + "-" * (max_len + 2) + "+")


if __name__ == "__main__":
    view_events()
