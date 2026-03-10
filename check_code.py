import requests
from key import KEY
import logging
logging.basicConfig(filename=f"E:\\Assignment\\Logs\\Check_code\\status1.log",
                    level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    force=True)
def status_code() -> int:

    HOST = "https://tg-f1599ec5-b595-4bc5-8466-beb036fadafb.tg-2635877100.i.tgcloud.io"
    API_KEY = KEY
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    # simple test endpoint
    url = f"{HOST}/restpp/echo"

    response = requests.get(url, headers=headers)

    data = response.json()
    return response.status_code
code=status_code()
if code == 200:
    logging.info(f"Status code: {code}")
else:
    logging.error(f"Status code: {code}")

