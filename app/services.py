import requests
from config import CLIENT_ID, CLIENT_SECRET, AUTH_URL, COMPANY_URL

def get_token():
    payload = {
        "clientID": CLIENT_ID,
        "clientSecret": CLIENT_SECRET
    }
    response = requests.post(AUTH_URL, json=payload)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception("Failed to get token: " + response.text)

def get_companies():
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(COMPANY_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch companies: " + response.text)
