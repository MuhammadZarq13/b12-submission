import json, hmac, hashlib, requests
from datetime import datetime

# 1. Prepare payload
payload = {
    "action_run_link": "https://github.com/MuhammadZarq13/ci-submission/actions/runs/1",
    "email": "devzarqkhan1@gmail.com",
    "name": "Zarq Khan",
    "repository_link": "https://github.com/MuhammadZarq13",
    "resume_link": "https://linkedin.com/in/devzarqkhan",
    "timestamp": datetime.utcnow().isoformat() + "Z"
}

# 2. Canonicalize JSON: sorted keys, compact separators
json_data = json.dumps(payload, sort_keys=True, separators=(',', ':')).encode('utf-8')

# 3. Compute HMAC-SHA256 signature
secret = b"hello-there-from-b12"
signature = hmac.new(secret, json_data, hashlib.sha256).hexdigest()
headers = {"X-Signature-256": f"sha256={signature}"}

# 4. POST request to B12
response = requests.post("https://b12.io/apply/submission", headers=headers, data=json_data)

# 5. Print submission receipt
print(response.text)
