from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta


# Load environment variables from .env.local
load_dotenv(dotenv_path=".env.local")

# Retrieve the variables
credentials_path = os.getenv("CREDENTIALS_PATH")
token_path = os.getenv("TOKEN_PATH")

# Initialize GoogleCalendar with the environment variables
gc = GoogleCalendar(
    credentials_path=credentials_path,
    token_path=token_path,
)


from datetime import datetime, timedelta

time_min = datetime.now() - timedelta(days=2)
time_max = datetime.now() + timedelta(days=6)

events = gc.get_events(time_min, time_max, order_by="startTime", single_events=True)

for event in events:
    print(event)
