import requests

url = "http://127.0.0.1:8000/api/register/"
data = {
    "email": "test@example.com",
    "username": "testuser",
    "password": "StrongPassword123"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
