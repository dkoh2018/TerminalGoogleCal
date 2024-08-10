import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from authenticate_calendar import authenticate_calendar
from openai import OpenAI
from colorama import Fore, Style, init
from llm_prompts import (
    system_delete_message_parameterdirections,
    system_delete_message_request,
)


def delete_an_event():
    # authenticate Google Calendar
    gc = authenticate_calendar()

    # user input
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{'='*50}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}📅 Delete an event")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'='*50}")

    # current date and time
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now()

    print(
        f"{Fore.GREEN}Today's Date: {current_date}: {current_time.strftime('%H:%M:%S')}"
    )
    print(f"{Fore.CYAN}{'-'*50}")
    while True:
        # prompt the user to choose between deleting past, upcoming, or recent events
        print(f"\n{Style.BRIGHT}{Fore.CYAN}Choose an option:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1) Delete future events{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2) Delete past events{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3) Delete most recent events{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4) Go back to main menu{Style.RESET_ALL}")
        choice = input(f"\n{Style.BRIGHT}Enter 1, 2, 3, or 4: {Style.RESET_ALL}")

        # determine the time range based on user choice
        if choice == "1":
            time_min = datetime.now()
            time_max = datetime.now() + timedelta(days=14)
            header = f"\n{Fore.GREEN}Delete future events from {time_min.date()} to {time_max.date()}:{Style.RESET_ALL}\n"
        elif choice == "2":
            time_min = datetime.now() - timedelta(days=14)
            time_max = datetime.now()
            header = f"\n{Fore.GREEN}Delete past events from {time_min.date()} to {time_max.date()}:{Style.RESET_ALL}\n"
        elif choice == "3":
            time_min = datetime.now() - timedelta(days=2)
            time_max = datetime.now() + timedelta(days=3)
            header = f"\n{Fore.GREEN}Delete most recent events from {time_min.date()} to {time_max.date()}:{Style.RESET_ALL}\n"
        elif choice == "4":
            print(f"{Fore.GREEN}Returning to main menu...{Style.RESET_ALL}")
            return
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
            continue

        # fetch events within the chosen time range
        events = list(
            gc.get_events(time_min, time_max, order_by="startTime", single_events=True)
        )

        # open a file to write the output
        with open("list_of_events.txt", "w") as file:
            output_header = header + "-" * 80 + "\n" + "-" * 80 + "\n"
            print(output_header)
            file.write(output_header)

            if not events:
                no_events_message = "{Fore.RED}No events found in the selected time range.{Style.RESET_ALL}\n"
                print(no_events_message)
                file.write(no_events_message)
            else:
                event_counter = 1
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
                    event_details = (
                        f"{Fore.CYAN}Event: {event_counter}{Style.RESET_ALL}\n"
                        f"   {Fore.YELLOW}EVENT_ID: {event.event_id}{Style.RESET_ALL}\n"
                        f"   {Fore.YELLOW}Summary: {Style.RESET_ALL}{event.summary}\n"
                        f"   {Fore.YELLOW}Start: {Style.RESET_ALL}{start_time}\n"
                        f"   {Fore.YELLOW}End: {Style.RESET_ALL}{end_time}\n"
                    )

                    if event.description:
                        event_details += f"   Description: {event.description}\n"

                    event_details += "-" * 80 + "\n"

                    # write to file and print to terminal
                    print(event_details)
                    file.write(event_details)

                    # increment the counter for the next event
                    event_counter += 1

        with open("list_of_events.txt", "r") as file:
            user_list = file.read()

        input_message = input(
            f"{Style.BRIGHT}{Fore.CYAN}Which item would you like to delete? Please enter a number: {Style.RESET_ALL}"
        )

        # Initiate LLM
        client = OpenAI()
        messages = [
            {
                "role": "system",
                "content": f"{system_delete_message_parameterdirections}",
            },
            {
                "role": "system",
                "content": f"{user_list}",
            },
            {
                "role": "system",
                "content": f"{system_delete_message_request}",
            },
            {
                "role": "user",
                "content": f"{input_message}",
            },
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.5,
        )

        make_action = response.choices[0].message.content

        # save the output to a file
        with open("llm_output.txt", "w") as file:
            file.write(make_action)

        system_summary = [
            {
                "role": "system",
                "content": "Your main goal is to look at this list and just paste exactly which event I chose to delete. I will give you the current list that I have and also give you the number that I'm choosing to delete.",
            },
            {
                "role": "system",
                "content": f"{user_list}",
            },
            {
                "role": "system",
                "content": f"Great now which number did you want to delete and i will provide only provide the snippet of information that you chose to delete as the output",
            },
            {
                "role": "user",
                "content": f"{input_message}",
            },
        ]

        summary = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=system_summary,
            temperature=0.5,
        )

        summarize_action = summary.choices[0].message.content

        # confirmation prompt before executing deletion since i keep making a mistake
        confirm_delete = (
            input(
                f"{Fore.RED}Are you sure you want to delete this event? (y/n): {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )

        if confirm_delete == "y":
            exec(make_action)
            print(
                f"\n{Fore.CYAN}Got it. I've successfully deleted this for you.\n\n{Style.RESET_ALL}{Fore.YELLOW}{summarize_action}{Style.RESET_ALL}"
            )
        else:
            print(f"\n{Fore.YELLOW}Cancelled...{Style.RESET_ALL}")

        # ask the user if they want to delete another event
        delete_another = (
            input(
                f"\n{Fore.CYAN}Do you want to delete another event? (y/n): {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if delete_another != "y":
            print(f"\n{Fore.YELLOW}Catch you later...{Style.RESET_ALL}")
            break


if __name__ == "__main__":
    delete_an_event()
