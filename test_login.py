import requests

url = "http://127.0.0.1:8000/api/login/"
data = {
    "email": "test@example.com",  # use your registered email
    "password": "StrongPassword123"  # use your actual password
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
