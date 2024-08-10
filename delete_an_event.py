import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from authenticate_calendar import authenticate_calendar
from openai import OpenAI


def delete_an_event():
    # Authenticate Google Calendar
    gc = authenticate_calendar()

    while True:
        # Prompt the user to choose between deleting past or upcoming events
        choice = input(
            "Choose an option: \n1) Delete past events\n2) Delete upcoming events\nEnter 1 or 2: "
        )

        # Determine the time range based on user choice
        if choice == "1":
            time_min = datetime.now()
            time_max = datetime.now() + timedelta(days=14)
            header = f"\nDelete upcoming events from {time_min.date()} to {time_max.date()}:\n"
        elif choice == "2":
            time_min = datetime.now() - timedelta(days=14)
            time_max = datetime.now()
            header = (
                f"\nDelete past events from {time_min.date()} to {time_max.date()}:\n"
            )
        else:
            print("Invalid choice. Exiting.")
            exit()

        # Fetch events within the chosen time range
        events = list(
            gc.get_events(time_min, time_max, order_by="startTime", single_events=True)
        )

        # Open a file to write the output
        with open("list_of_events.txt", "w") as file:
            output_header = header + "-" * 80 + "\n" + "-" * 80 + "\n"
            print(output_header)
            file.write(output_header)

            if not events:
                no_events_message = "No events found in the selected time range.\n"
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
                        f"{event_counter}. EVENT_ID: {event.event_id}\n"
                        f"   Summary: {event.summary}\n"
                        f"   Start: {start_time}\n"
                        f"   End: {end_time}\n"
                    )

                    if event.description:
                        event_details += f"   Description: {event.description}\n"

                    event_details += "-" * 80 + "\n"

                    # Write to file and print to terminal
                    print(event_details)
                    file.write(event_details)

                    # Increment the counter for the next event
                    event_counter += 1

        # Predefined system prompts
        system_message_parameterdirections = """
        You will be given a txt file with a list of events. Each event has an ID and is ordered. Based on the order, you must locate the EVENT_ID.
        """

        with open("list_of_events.txt", "r") as file:
            user_list = file.read()

        system_message_request = """
        Thank you for providing the list. Now that we have the list in order, please specify the number of the event you'd like to delete. Once you provide the number, I will locate the corresponding `EVENT_ID` and present it as a variable called `eventID`. Then, I will execute the command `gc.delete_event(eventID)`.

        The final output should look like this:
        eventID = "_60sjih9g8gskcb9p60pjab9k8kr3cba18kpj0b9h6ssk6dhm8p132c9n60_20240809"
        gc.delete_event(eventID)

        ALWAYS ENSURE NO MATTER WHAT that the output is not in code blocks with ```PYTHON```, and make sure there is no extra spacing before or after the `eventID` string.
        """

        input_message = input(
            "Which item would you like to delete? Please enter a number: "
        )

        # Initiate LLM
        client = OpenAI()
        messages = [
            {
                "role": "system",
                "content": f"{system_message_parameterdirections}",
            },
            {
                "role": "system",
                "content": f"{user_list}",
            },
            {
                "role": "system",
                "content": f"{system_message_request}",
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

        # Save the output to a file
        with open("llm_output.txt", "w") as file:
            file.write(make_action)

        exec(make_action)

        # Ask the user if they want to delete another event
        delete_another = (
            input("Do you want to delete another event? (y/n): ").strip().lower()
        )
        if delete_another != "y":
            print("catch you later...")
            break


if __name__ == "__main__":
    delete_an_event()
