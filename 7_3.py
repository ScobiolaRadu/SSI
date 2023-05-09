import hashlib
import requests

file_path = "C:/Users/RaduScobiolaKodingTe/Downloads/lab_9.ipynb"

with open(file_path, 'rb') as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()

api_key = "33c1562054d9a2f6f36fa354cdc587b5050dda058b7d87a3b80decd198da0b9c"
url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
headers = {
    "x-apikey": api_key,
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "gzip"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    json_response = response.json()
    detections = json_response["data"]["attributes"]["last_analysis_stats"]["malicious"]
    print(f"Anti-virus vendors which detect the file: {detections}")
else:
    print(f"Error: {response.status_code} - {response.text}")
