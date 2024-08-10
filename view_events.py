from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from authenticate_calendar import authenticate_calendar
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def view_events():
    gc = authenticate_calendar()

    # Prompt the user to select a time range
    print(f"\n{Style.BRIGHT}{Fore.CYAN}Select a time range option:{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}  1) Next 2 weeks from today{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}  2) Past 2 weeks from today{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}  3) Past week and this week{Style.RESET_ALL}\n")
    choice = input(f"{Style.BRIGHT}Enter the option number (1/2/3): {Style.RESET_ALL}")

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
        print(f"{Fore.RED}Invalid choice. Please select 1, 2, or 3.{Style.RESET_ALL}")
        return

    events = list(
        gc.get_events(time_min, time_max, order_by="startTime", single_events=True)
    )

    if not events:
        print(f"{Fore.RED}No events found in the selected time range.{Style.RESET_ALL}")
        return

    print(
        f"\n{Style.BRIGHT}{Fore.CYAN}Events from {time_min.date()} to {time_max.date()}:{Style.RESET_ALL}"
    )
    print(f"{Fore.YELLOW}{'-' * 80}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'-' * 80}{Style.RESET_ALL}")

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

        print(f"{Fore.CYAN}Summary: {Style.RESET_ALL}{event.summary}")
        print(f"{Fore.CYAN}Start: {Style.RESET_ALL}{start_time}")
        print(f"{Fore.CYAN}End: {Style.RESET_ALL}{end_time}")

        if event.description:
            print(f"{Fore.CYAN}Description: {Style.RESET_ALL}{event.description}")
        print(f"{Fore.YELLOW}{'-' * 80}{Style.RESET_ALL}")


if __name__ == "__main__":
    view_events()
