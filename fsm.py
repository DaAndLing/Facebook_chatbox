from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url
from one_pic import pic_url, pic_url_limit
from weather import weather
from google import google
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    #judge if input string is in grammar
    def is_going_to_weather_state(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == '天氣'
        return False

    def is_going_to_dcard_state(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'dcard'
        return False

    def is_going_to_google_state(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'google'
        return False

    def is_goint_to_pet_state(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'pet'
        return False

    def is_goint_to_sex_state(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'sex'
        return False

    def is_goint_to_pet_limit_state(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower().isdigit()
        return False

    def is_goint_to_pet_unlimit_state(self, event):
        if event.get("message"):
           text = event['message']['text']
           return not text.lower().isdigit()
        return False

    def is_goint_to_sex_limit_state(self, event):
        if event.get("message"):
           text = event['message']['text']
           return text.lower().isdigit()
        return False

    def is_goint_to_sex_unlimit_state(self, event):
        if event.get("message"):
            text = event['message']['text']
            return not text.lower().isdigit()
        return False

    def on_enter_user_state(self, event):
        print("I'm entering User state")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "還有想做的事情嘛？")

    def on_enter_weather_state(self, event):
        print("I'm entering weather state")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "你想查詢的城市是？")

    def on_enter_weather_city_state(self, event):
        print("I'm entering weather city state")
        sender_id = event['sender']['id']
        city_url = weather(event['message']['text'])
        send_text_message(sender_id, "以下是中央氣象局:" + event['message']['text'])
        send_text_message(sender_id, city_url)
        self.go_back(event)

    def on_enter_dcard_state(self, event):
        print("I'm entering dcard state")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "你想找的圖片是?")

    def on_enter_pet_state(self, event):
        print("I'm entering pet state")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "讚數限制？(數字 or 隨意)")

    def on_enter_pet_limit_state(self, event):
        print("I'm entering pet limit state")
        sender_id = event['sender']['id']
        url = pic_url_limit("pet", int(event['message']['text']))
        if url == 'Not found':
            responese = send_text_message(sender_id, "太貪心囉~")
            responese = send_text_message(sender_id, "短時間內沒辦法幫你找到")
        else:
            responese = send_text_message(sender_id, "From Dcard~")
            responese = send_image_url(sender_id, url)
        self.go_back(event)

    def on_enter_pet_unlimit_state(self, event):
        print("I'm entering pet unlimit state")
        sender_id = event['sender']['id']
        url = pic_url("pet")
        responese = send_text_message(sender_id, "From Dcard~")
        responese = send_image_url(sender_id, url)
        self.go_back(event)
        
    def on_enter_sex_state(self, event):
        print("I'm entering sex state")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "讚數限制？(數字 or 隨意)")

    def on_enter_sex_limit_state(self, event):
        print("I'm entering sex limit state")
        sender_id = event['sender']['id']
        url = pic_url_limit("sex", int(event['message']['text']))
        responese = send_text_message(sender_id, "Sex limit~")
        if url == 'Not found':
            responese = send_text_message(sender_id, "太貪心囉~")
            responese = send_text_message(sender_id, "短時間內沒辦法幫你找到")
        else:
            responese = send_text_message(sender_id, "From Dcard~")
            responese = send_image_url(sender_id, url)
        self.go_back(event)

    def on_enter_sex_unlimit_state(self, event):
        print("I'm entering sex unlimit state")
        sender_id = event['sender']['id']
        url = pic_url("sex")
        responese = send_text_message(sender_id, "From Dcard~")
        responese = send_image_url(sender_id, url)
        self.go_back(event)

    def on_enter_google_state(self, event):
        print("I'm entering google state")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "你想Google的是?")

    def on_enter_google_search_state(self, event):
        print("I'm entering google search state")
        sender_id = event['sender']['id']
        search_result = google(event['message']['text'])
        send_text_message(sender_id, "我們幫你從Google找到：")
        send_text_message(sender_id, search_result)
        self.go_back(event)