from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from authenticate_calendar import authenticate_calendar


def view_events():
    gc = authenticate_calendar()

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

    if not events:
        print("No events found in the selected time range.")
        return

    print(f"\nEvents from {time_min.date()} to {time_max.date()}:")
    print("-" * 80)
    print("-" * 80)

    for event in events:
        start_time = (
            event.start.strftime("%Y-%m-%d %H:%M")
            if isinstance(event.start, datetime)
            else event.start
        )
        end_time = (
            event.end.strftime("%Y-%m-%d %H:%M")
            if isinstance(event.end, datetime)
            else event.end
        )

        print(f"Summary: {event.summary}")
        print(f"Start: {start_time}")
        print(f"End: {end_time}")

        if event.description:
            print(f"Description: {event.description}")
        print("-" * 80)


if __name__ == "__main__":
    view_events()
