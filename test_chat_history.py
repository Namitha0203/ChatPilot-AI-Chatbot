import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4NDkzMzMyLCJpYXQiOjE3NTg0OTMwMzIsImp0aSI6IjQ2N2RkMTQ0ZmMwODRmMGNhZDYzNzdiYThlOTJiNzZkIiwidXNlcl9pZCI6IjEifQ.a2WCSM9W1cXYwCUH-8oPP2ww0p2mUZIOM-b0N3FTodY",   # your real token
    "Content-Type": "application/json"
}

response = requests.get("http://127.0.0.1:8000/api/chat/history/", headers=headers)
print(response.status_code)
print(response.json())
