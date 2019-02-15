import requests
import settings


def get_kayako_auth():
    return (settings.KAYAKO_USER, settings.KAYAKO_PASSWORD)


def get_message_payload(message):
    return {
        "contents": message,
        "channel": "MAIL",
        "channel_id": 1
    }


def get_reply_endpoint(case_id):
    base_api = settings.KAYAKO_API_ENDPOINT
    return "/".join([base_api, 'cases', case_id, 'reply.json'])


def send_message(case_id, message):
    payload = get_message_payload(message)
    reply_endpoint = get_reply_endpoint(case_id)
    r = requests.post(reply_endpoint, json=payload, auth=get_kayako_auth())
    print(r.headers)
    print(r.content)
