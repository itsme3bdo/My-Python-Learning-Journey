import requests
from datetime import datetime

USERNAME = "abdothegreat"
TOKEN = "abefelikfdaklsn"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
graphh_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id":GRAPHID,
    "name":"Productive Hours",
    "unit":"Hours",
    "type":"float",
    "color":"kuro"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

add_data_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many hours did you work today?")
}
# response = requests.post(url=add_endpoint, json=add_data_config, headers=headers)
# print(response.text)

change_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20241230"

update_config = {
    "quantity":"2"
}
## PUT
# response = requests.put(url=change_endpoint, json=update_config, headers=headers)
# print(response.text)

headers = {
    "X-USER-TOKEN":TOKEN
}
color = {
    "color":"ajisai"
}


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

