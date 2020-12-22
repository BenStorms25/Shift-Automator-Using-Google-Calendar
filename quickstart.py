from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = "Client_Secret_New.json"
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def createCalendar(service, Name):

    """ 
    Creates a calendar.

    """

    request_body = {
    'summary': Name
    }
    response = service.calendars().insert(body = request_body).execute()
    print(response)

def deleteCalendar(service, IdString):

    """
    Deletes a calendar by ID.

    """

    service.calendars().delete(calendarId=IdString).execute()

event = {
  'summary': 'Final Exam',
  
  'description': 'It\'s the exam',
  'start': {
    'dateTime': '2020-12-24T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2020-12-24T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

event = service.events().insert(calendarId='primary', body=event).execute()