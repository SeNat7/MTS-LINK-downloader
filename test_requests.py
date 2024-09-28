import requests


params = {"withoutCuts": "false"}
response = requests.get(f"https://my.mts-link.ru/api/eventsessions/257884186/record?withoutCuts=false&recordAccessToken=ab87d25acad94efc94b9a30a19f91e0b",
   params=params)
data = response.json()
event_logs = data["name"]
print(event_logs)
