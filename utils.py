import requests
import os

GRAPH_URL = "https://graph.facebook.com/v3.1"
# ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN = "EAAfwXNSFdh0BAGdzwU4I3mVZB0HFiSZBQZCeDhMhtXyzlvLdjuJxofOLPDhDVAyZCOrWeDopMhZAcimiBiVvjogN03qaZBnua0JQcKjNOIvK8qAykiaqFVZAZCnbl1WPaCPerlVZAcoHQu6Kb0tRdcjqQdfOMNFjSpQ9cFtxBWMFfFQZDZD"

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"attachment":{"type":"image",
                                        "payload":{"url":img_url,
                                                    "is_reusable": True }
                    }
                }
            }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

"""
def send_button_message(id, text, buttons):
    pass
"""
