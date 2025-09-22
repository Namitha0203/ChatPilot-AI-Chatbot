import requests

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

data = {
    "model": "meta-llama/llama-3-8b-instruct",  # ✅ Valid model ID
    "messages": [
        {"role": "user", "content": "Hello! How are you?"}
    ]
}


response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

print(response.status_code)
print(response.json())
