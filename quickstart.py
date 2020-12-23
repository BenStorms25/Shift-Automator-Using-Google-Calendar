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
    calID = response['id']
    print(response)
    return calID

def deleteCalendar(service, IdString):

    """
    Deletes a calendar by ID.

    """

    service.calendars().delete(calendarId=IdString).execute()

# event = {
#   'summary': 'Final Exam',
  
#   'description': 'It\'s the exam',
#   'start': {
#     'dateTime': '2020-12-29T04:00:00-07:00',
#     'timeZone': 'America/New_York',
#   },
#   'end': {
#     'dateTime': '2020-12-29T5:00:00-07:00',
#     'timeZone': 'America/New_York',
#   },
#   'recurrence': [
#     'RRULE:FREQ=DAILY;COUNT=1'
#   ],
#   'attendees': [
#     {'email': 'lpage@example.com'},
#     {'email': 'sbrin@example.com'},
#   ],
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }

# service.events().insert(calendarId='mhj5hgpvpjs6g7po8pvj3r7q6c@group.calendar.google.com', body=event).execute()
#event = 
def insertEvent(service, calendarId, startDate = '2020-12-29', endDate = '2020-12-29', startTime = '04:00:00-07:00', endTime = '5:00:00-07:00'):
  event = {
    'summary': 'Final Exam',
  
    'description': 'It\'s the exam',
    'start': {
      'dateTime': startDate + 'T' + startTime,
      'timeZone': 'America/New_York',
    },
    'end': {
      'dateTime': '2020-12-29T5:00:00-07:00',
      'timeZone': 'America/New_York',
    },
    'recurrence': [
      'RRULE:FREQ=DAILY;COUNT=1'
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

  service.events().insert(calendarId='mhj5hgpvpjs6g7po8pvj3r7q6c@group.calendar.google.com', body=event).execute()



calID = createCalendar(service, "Final Dates")
insertEvent(service, calID,startDate = '2020-12-29',endDate='2020-12-29',)