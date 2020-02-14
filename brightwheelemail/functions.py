import requests

from brightwheel import settings


def send_simple_message(to_email: str, from_email: str, subject: str,
                        body: str):
    if settings.EMAIL_PROVIDER == 'mailgun':
        return requests.post(settings.EMAIL_URL,
                             auth=("api", settings.API_KEY),
                             data={"from": from_email,
                                   "to": to_email,
                                   "subject": subject,
                                   "html": body}
                             )
    elif settings.EMAIL_PROVIDER == 'sendgrid':
        return requests.post(settings.EMAIL_URL,
                             headers={
                                 "Authorization": f'Bearer {settings.API_KEY}',
                                 'Content-type': 'application/json'
                             },
                             json={
                                 "personalizations": [
                                     {
                                         "to":
                                             [
                                                {"email": to_email}
                                             ]
                                     }
                                 ],
                                 "from": {"email": from_email},
                                 "subject": subject,
                                 "content": [
                                     {"type": "text/html", "value": body}
                                 ]
                             }
                             )
