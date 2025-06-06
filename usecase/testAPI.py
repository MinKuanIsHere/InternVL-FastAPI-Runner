import os
from dotenv import load_dotenv
import requests

load_dotenv()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
url = f"http://{HOST}:{PORT}"

# Test root ("/")
try:
    res = requests.get(url)
    print(f"[/] Status Code: {res.status_code}")
    print(res.json())
except requests.exceptions.RequestException as e:
    print(f"[/] Connection error: {e}")

# Test /ping
try:
    res = requests.get(f"{url}/ping")
    print(f"[/ping] {res.json()}")
except requests.exceptions.RequestException as e:
    print(f"[/ping] Connection error: {e}")

# Test /gpu
try:
    res = requests.get(f"{url}/gpu")
    print(f"[/gpu] {res.json()}")
except requests.exceptions.RequestException as e:
    print(f"[/gpu] Connection error: {e}")
