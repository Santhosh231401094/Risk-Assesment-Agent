import requests
import json

url = "https://api.mistral.ai/v1/chat/completions"


api_key = "cmxQnA1qscRP9k22Rz5cebUlcJqTQW8M"


headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


prompt = """
I am planning to make a startup on e-learning.
What are the potential risks involved?
Please provide the answer strictly in the following JSON format:

{
  "technical_risks": [],
  "market_risks": [],
  "legal_risks": [],
  "funding_risks": [],
  "execution_risks": [],
  "mitigation_strategies": {
    "privacy": "",
    "tech": ""
  }
}
"""

payload = {
    "model": "mistral-large-latest",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)


print("Status Code:", response.status_code)


if response.status_code == 200:
    try:
       
        raw_content = response.json()['choices'][0]['message']['content']

        json_start = raw_content.find('{')
        json_end = raw_content.rfind('}') + 1
        json_content = raw_content[json_start:json_end]

        
        structured_output = json.loads(json_content)

      
        print(json.dumps(structured_output, indent=2))

    except Exception as e:
        print("Error parsing JSON:", e)
        print("Raw content from model:")
        print(raw_content)
else:
    print("Error:", response.text)
