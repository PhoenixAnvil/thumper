import requests

def ping_api(url, count):
    if count is None:
        while True:
            requests.get(url)

    for _ in range(count):
        requests.get(url)
