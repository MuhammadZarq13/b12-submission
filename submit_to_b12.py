import json, hmac, hashlib, requests
from datetime import datetime

SIGNING_SECRET = b"hello-there-from-b12"
NAME = "Zarq Khan"
EMAIL = "devzarqkhan1@gmail.com"
RESUME_LINK = "https://www.linkedin.com/in/devzarqkhan/"
REPOSITORY_LINK = "https://github.com/MuhammadZarq13/b12-submission"
ACTION_RUN_LINK = "https://github.com/MuhammadZarq13/b12-submission/actions/runs/REPLACE_WITH_RUN_ID"
SUBMISSION_URL = "https://b12.io/apply/submission"


payload = {
    "action_run_link": ACTION_RUN_LINK,
    "email": EMAIL,
    "name": NAME,
    "repository_link": REPOSITORY_LINK,
    "resume_link": RESUME_LINK,
    "timestamp": datetime.utcnow().isoformat() + "Z"
}

payload_bytes = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")


signature = hmac.new(SIGNING_SECRET, payload_bytes, hashlib.sha256).hexdigest()
headers = {"X-Signature-256": f"sha256={signature}"}

response = requests.post(SUBMISSION_URL, headers=headers, data=payload_bytes)
print(response.text)
