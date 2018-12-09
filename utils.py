import requests
import os

GRAPH_URL = "https://graph.facebook.com/v3.1"
ACCESS_TOKEN = "EAAfwXNSFdh0BAObRIwTVgL5LcYhB8uKithh8EXZBkuNsztQNgc2s5uPMw7YLYlguKlOCgpCm7zoZA9LKlk5LKCa14NZCYwyPL100CRVbiJbp94q3xY8p1Q47iTWNOlCPajyJUM6eGf0n2tAflWQ5CqEYrqGdXB4nAHipEdDPwZDZD$"


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


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""