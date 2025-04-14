import requests
import json

url = "https://api.together.xyz/v1/chat/completions"

api_key = "f7868dd1750bc150bb2c51decf007a5909a66436d129e37b964c38562075ac90"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

prompt = """
I am planning to make a startup on quick commerce.
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
    "model": "meta-llama/Llama-3-8b-chat-hf",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.7,
    "max_tokens": 1024
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
