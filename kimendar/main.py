from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
# If modifying these scopes, delete the file token.json.
from kimendar import SCOPE_READONLY, SCOPE


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials2.json', SCOPE)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    event = {
        'summary': 'Test Task',
        'location': 'Перервинский бульвар 2, корпус 1',
        'description': 'Test description of the task',
        'start': {
            'dateTime': '2018-12-20T09:00:00+03:00',
        },
        'end': {
            'dateTime': '2018-12-20T17:00:00+03:00',
        }
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(event)
    # print('Event created: %s' % (event.get('htmlLink')))
    # print('Getting the upcoming 10 events')
    # events_result = service.events().list(calendarId='primary', timeMin=now,
    #                                       maxResults=10, singleEvents=True,
    #                                       orderBy='startTime').execute()
    # events = events_result.get('items', [])

    # if not events:
    #     print('No upcoming events found.')
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])


if __name__ == '__main__':
    main()
