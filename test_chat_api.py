import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4NDkyNjE0LCJpYXQiOjE3NTg0OTIzMTQsImp0aSI6ImI3ZjAzNGM1YWU0ZTRiNWZhMTMwOWMxZTQzMGYzY2Y4IiwidXNlcl9pZCI6IjEifQ.GwVK8g8kx1MMgEm2N4TQYxsjIn8jkNK0x0W8O0dmYJE",  # your real token here
    "Content-Type": "application/json"
}

data = {
    "prompt": "Tell me something cool about volcanoes."
}

response = requests.post("http://127.0.0.1:8000/api/chat/", headers=headers, json=data)
print(response.status_code)
print(response.json())

