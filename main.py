from add_new_event import add_new_event
from delete_an_event import delete_an_event
from view_events import view_events
from settings import calendar_settings
from summarize_today import summarize_today
from see_ya import see_ya
from colorama import Fore, Style, init
from gcal_logo import gcal_logo

# Initialize colorama
init(autoreset=True)


def main_menu():
    while True:
        print(f"\n{Style.BRIGHT}What would you like to do today?{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. Add new event(s){Style.RESET_ALL}")
        print(f"{Fore.CYAN}2. Summarize my day{Style.RESET_ALL}")
        print(f"{Fore.CYAN}3. Delete event{Style.RESET_ALL}")
        print(f"{Fore.CYAN}4. View events{Style.RESET_ALL}")
        print(f"{Fore.CYAN}5. User Settings{Style.RESET_ALL}")
        print(f"{Fore.CYAN}6. Exit{Style.RESET_ALL}")

        choice = input(f"\n{Style.BRIGHT}Enter your choice (1-6): {Style.RESET_ALL}")

        if choice == "1":
            add_new_event()
        elif choice == "2":
            summarize_today()
        elif choice == "3":
            delete_an_event()
        elif choice == "4":
            view_events()
        elif choice == "5":
            calendar_settings()
        elif choice == "6":
            see_ya()
            break
        else:
            print(f"\n{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")


if __name__ == "__main__":
    print(gcal_logo)
    main_menu()
