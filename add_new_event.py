from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
from datetime import datetime
from beautiful_date import Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sept, Oct, Nov, Dec
from beautiful_date import hours
from openai import OpenAI
import os
from dotenv import load_dotenv
from authenticate_calendar import authenticate_calendar
from colorama import Fore, Style, init
from llm_prompts import (
    system_message_parameterdirections,
    system_message_directions,
    system_message_request,
)


def add_new_event():
    gc = authenticate_calendar()

    # user input
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{'='*50}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}📅 Add New Event")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'='*50}")

    # current date and time
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now()

    print(
        f"{Fore.GREEN}Today's Date: {current_date}: {current_time.strftime('%H:%M:%S')}"
    )
    print(f"{Fore.CYAN}{'-'*50}")

    user_input = input(
        f"{Fore.YELLOW}{Style.BRIGHT}What event(s) did you want to add? \n==> {Style.RESET_ALL}"
    )
    # Combine current time with user input
    user_message = f"{current_time}: {user_input}."

    # initiate llm
    client = OpenAI()
    messages = [
        {
            "role": "system",
            "content": f"{system_message_parameterdirections}",
        },
        {
            "role": "system",
            "content": f"{system_message_directions}",
        },
        {
            "role": "system",
            "content": f"{system_message_request}",
        },
        {
            "role": "user",
            "content": f"{user_message}",
        },
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.5,
    )

    make_action = response.choices[0].message.content

    # Save the output to a file
    with open("llm_output.txt", "w") as file:
        file.write(make_action)

    exec(make_action)

    # summarize events added
    with open("llm_output.txt", "r") as file:
        added_events = file.read()

    system_request2 = """
    I will quickly summarize the events added for you in a simple list. Make sure to include the event title, start/end time, and description (if available) that's easy to read. You will see the output something similar to this:
    
    Great! I've added these events for you:
    1) Testing Application  
       Start: August 9, 2024, 8:00 PM  
       End: August 9, 2024, 10:00 PM  

    2) Hiking with Mocha  
       Start: August 10, 2024, 8:00 AM  
       End: August 10, 2024, 3:00 PM  
    
    Successfully added...
    Let's continue...
    """
    messages2 = [
        {
            "role": "system",
            "content": f"{system_request2}",
        },
        {
            "role": "user",
            "content": f"{added_events}",
        },
    ]

    response2 = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages2,
        temperature=0.5,
    )

    print("\n")
    print(response2.choices[0].message.content)


if __name__ == "__main__":
    add_new_event()
