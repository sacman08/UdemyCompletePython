import requests
import json


def get_iss_loc_json():
    iss_location = requests.get('http://api.open-notify.org/iss-now.json')
    current_loc = json.loads(iss_location.content)
    return current_loc


my_loc = get_iss_loc_json()
print(type(my_loc))
print(my_loc["iss_position"])

