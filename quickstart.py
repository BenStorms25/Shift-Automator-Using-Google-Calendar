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
