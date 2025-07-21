import requests
import os

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_alert(message: str):
    """
    Send an alert message to Slack channel using Incoming Webhook.
    """
    if not SLACK_WEBHOOK_URL:
        print("Slack webhook URL not configured.")
        return

    payload = {
        "text": message
    }

    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        if response.status_code != 200:
            print(f"Failed to send Slack alert: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Exception while sending Slack alert: {e}")
