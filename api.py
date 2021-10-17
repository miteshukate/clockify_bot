import requests
import file_reader
from datetime import datetime,timedelta
import pytz
from dotenv import dotenv_values


API_ENDPOINT = "http://pastebin.com/api/api_post.php"

# your API key here
config = dotenv_values(".env")
API_KEY = config["CLOCKIFY_SECRETE"]



def getTimeEntryRequestPayload(start_end_date, description):
    # todo: dummy implementation
    local = pytz.timezone('Asia/Kolkata')

    return {
        "start": local.localize(start_end_date[0], is_dst=None).astimezone(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "billable": "true",
        "description": description,
        "taskId": None,
        "end": local.localize(start_end_date[1], is_dst=None).astimezone(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tagIds": None,
        "customFields": []
    }


def get_workspace():
    # implementation later
    workspaceId = "5bbc6e41b079870146f7aaec"
    url = "https://api.clockify.me/api/v1/workspaces"
    headers = {"Content-Type": "application/json",
               "X-Api-Key": API_KEY}

    response = requests.get(url,headers=headers)

    return response.json()

def get_project_id(workspaceId):
    # implementation later
    url = f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/projects"
    headers = {"Content-Type": "application/json",
               "X-Api-Key": API_KEY}

    response = requests.get(url,headers=headers)

    return response.json()


def create_time_entries():
    entries = file_reader.get_time_entries()
    print("********************** Started filling time sheet ******************")
    beg_date = datetime.now()
    for entry in entries:
        updated_date = get_date_time(beg_date)
        beg_date = updated_date[0]
        data = getTimeEntryRequestPayload(updated_date, entry)
        createTimeEntry(data)
        beg_date = beg_date + timedelta(days=1)
    print("********************** Completed filling time sheet ****************")



def createTimeEntry(data):
    workspaces = get_workspace()
    if len (workspaces) != 1:
        print("More than one workspaces")
        return

    workspaceId = workspaces[0]["id"]
    # project_id = get_project_id(workspaceId)
    url = f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/time-entries"
    headers = {"Content-Type": "application/json",
               "X-Api-Key": API_KEY}
    data["projectId"] = "5d831336affb256595167f1b"
    response = requests.post(url, headers=headers, json=data)
    print("response", response)


def get_date_time(dt):
    if dt.weekday() == 5:
        dt = dt + timedelta(days=2)
    if dt.weekday() == 6:
        dt = dt + timedelta(days=1)

    start_time = dt.replace(hour=9, minute=00)
    end_time = dt.replace(hour=18, minute=00)
    return start_time, end_time
