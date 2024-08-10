# terminal google calendar using openai

this project utilizes the `gcsa` package for google calendar integration and openai for generating event details. ensure you have an openai api key to use this functionality.

- add new events to your google calendar
- delete events from your calendar
- view existing events
- manage calendar settings

## you'l need

- python 3.x
- google calendar api credentials.json (oauth)

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
