import requests
from dotenv import load_dotenv
import os 

load_dotenv()
url = os.getenv("URL")
r = requests.get(url)


if r.status_code >= 400: 
    print(r.status_code)
    print(r.headers)
    raise RuntimeError(f'curl request to {url} was not successful. status code: {r.status_code}')
else:
    print(f"All good. curl request to {url} returned status code {r.status_code}")