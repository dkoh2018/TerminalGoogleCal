from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os
from datetime import datetime
from authenticate_calendar import authenticate_calendar

# initialize GoogleCalendar with the environment variables
gc = authenticate_calendar()


event_id_to_delete = "s9uh3n1f7cuvhmu4hcguco34d0"
gc.delete_event(event_id_to_delete)
