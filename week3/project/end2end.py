import json
import requests
if __name__ == '__main__':
    queries = []
    with open('project/data/requests.json', 'r') as f:
        queries = [json.loads(line) for line in f]

    endpoint = "http://0.0.0.0:8000/predict"
    for q in queries:
        print(requests.post(endpoint, data=json.dumps(q)).json())