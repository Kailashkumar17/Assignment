import requests
from key import KEY


def status_code():

    HOST = "https://tg-f1599ec5-b595-4bc5-8466-beb036fadafb.tg-2635877100.i.tgcloud.io"
    API_KEY = KEY
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{HOST}/restpp/echo"
    response = requests.get(url, headers=headers)
    data = response.json()
    return response.status_code
