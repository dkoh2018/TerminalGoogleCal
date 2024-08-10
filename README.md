# terminal google calendar using openai

this project utilizes the `gcsa` package for google calendar integration and openai for generating event details. ensure you have an openai api key to use this functionality.

- add new events to your google calendar
- delete events from your calendar
- view existing events
- manage calendar settings

## you'l need

- python 3.x
- google calendar api credentials.json (oauth)

## Setting up credentials

1. Create a directory called `credentials` in your project root.
2. Add your `credentials.json` file to the `credentials` directory.
3. Create a `.env.local` file in your project root with the following content:

   ```
   CREDENTIALS_PATH=/path/to/your/project/credentials/credentials.json
   TOKEN_PATH=/path/to/your/project/credentials/token.pickle
   ```

   Replace `/path/to/your/project` with the actual path to your project directory.

4. The `token.pickle` file will be automatically generated when you first authenticate with Google Calendar.

Make sure to update the `authenticate_calendar.py` file to use these environment variables for authentication.

if you have a credentials.json (client*secret*\*.json) file (see getting started), googlecalendar will read all the needed data to generate the token and refresh-token from it.

to read credentials.json (client*secret*\*.json) from the default directory (~/.credentials) use:

```python
gc = googlecalendar()
```

## usage

run main script:

```bash
python main.py
```

follow the on-screen prompts to interact with your google calendar.

## file structure

- `main.py`: entry point of the application
- `add_new_event.py`: handles adding new events to the calendar
- `delete_an_event.py`: manages event deletion
- `view_events.py`: displays calendar events
- `settings.py`: manages calendar settings

contributions are welcome. please open an issue or submit a pull request.
