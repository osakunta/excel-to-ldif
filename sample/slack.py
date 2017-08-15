import requests, json
from data.data import slack_channel
from data.data import slack_webhook_url

# Uses 'requests' library to send a http POST request to 'webhook_url' with a body 'message'
def send_slack_notification(message):
    headers = {'Content-type': 'application/json'}
    request = requests.post(slack_webhook_url, headers=headers, data=json.dumps(message))

    print(request.status_code)
    print(request.content)

# Return a dictionary which represents JSON body of the Slack notification POST request
# Documentation can be found here: https://api.slack.com/docs/messages
def slack_message(error, reason, where, line):
     return {
        "channel": slack_channel,
        "username": "Mailing List Generator",
        "icon_emoji": ":warning:",
        "attachments": [
            {
                "fallback": error,
                "color": "warning",
                "title": error,
                "text": reason + '\nTaulukossa: ' + where + '\nRivillä: ' + line
            }
        ]
    }
