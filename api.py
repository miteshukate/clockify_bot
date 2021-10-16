import requests
import json
import datetime

API_ENDPOINT = "http://pastebin.com/api/api_post.php"

# your API key here
API_KEY = "XXXXXXXXXXXXXXXXX"


def getTimeEntryRequestPayload():
    # todo: dummy implementation
    return {
        "start": "2021-10-20T13:48:14.000Z",
        "billable": "true",
        "description": "Testing the project with the given data",
        "projectId": "5d831336affb256595167f1b",
        "taskId": None,
        "end": "2021-10-20T13:50:10.000Z",
        "tagIds": None,
        "customFields": []
    }


def getWorkspace():
    # implementation later
    pass


def createTimeEntry():
    workspaceId = "5bbc6e41b079870146f7aaec"
    api_key = ""
    url = f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/time-entries"
    headers = {"Content-Type": "application/json",
               "X-Api-Key": api_key}

    data = getTimeEntryRequestPayload()

    response = requests.post(url, headers=headers, json=data)
    print("response", response)
