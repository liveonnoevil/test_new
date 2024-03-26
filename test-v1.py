import requests
API_TOKEN = "xxx"
API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

proxy={
    'http':'127.0.0.1:7897',
    'https':'127.0.0.1:7897'
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload, proxies=proxy)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})
print(f'{output}')