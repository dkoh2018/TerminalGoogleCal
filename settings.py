import os
from dotenv import load_dotenv
from gcsa.google_calendar import GoogleCalendar
from colorama import Fore, Style, init
from authenticate_calendar import authenticate_calendar


def calendar_settings():
    # Construct the path to .env.local in the parent directory
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env.local")
    load_dotenv(dotenv_path=env_path)

    # Retrieve the variables
    credentials_path = os.getenv("CREDENTIALS_PATH")
    token_path = os.getenv("TOKEN_PATH")

    # Initialize GoogleCalendar with the environment variables
    gc = GoogleCalendar(
        credentials_path=credentials_path,
        token_path=token_path,
    )

    settings = gc.get_settings()
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{'='*50}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}⚙️ User Settings")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'='*50}")

    print(f"{settings}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'='*50}")
    print(
        f"\n{Fore.YELLOW}...is there anything else you'd like to do?{Style.RESET_ALL}\n"
    )


if __name__ == "__main__":
    calendar_settings()
