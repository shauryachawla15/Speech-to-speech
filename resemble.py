import requests

API_KEY = "PASTE_YOUR_REAL_API_TOKEN_HERE"

url = "https://app.resemble.ai/api/v2/voices?page=1&page_size=5"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)