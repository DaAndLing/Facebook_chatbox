from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url
from one_pic import pic_url
from weather import weather

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

    def on_enter_user_state(self):
        print("I'm entering User state")

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
        self.go_back()

    def on_enter_dcard_state(self, event):
        print("I'm entering dcard state")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "你想找的圖片是?(Pet or Sex)")

    def on_enter_pet_state(self, event):
        print("I'm entering pet state")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "讚數限制？(數字 or 隨意)")

    def on_enter_pet_limit_state(self, event):
        print("I'm entering pet limit state")
        sender_id = event['sender']['id']
        # url = pic_url("pet")
        responese = send_text_message(sender_id, "Pet limit~")
        # responese = send_text_message(sender_id, "From Dcard~")
        # responese = send_image_url(sender_id, url)
        self.go_back()

    def on_enter_pet_unlimit_state(self, event):
        print("I'm entering pet unlimit state")
        sender_id = event['sender']['id']
        url = pic_url("pet")
        responese = send_text_message(sender_id, "From Dcard~")
        responese = send_image_url(sender_id, url)
        self.go_back()
        
    def on_enter_sex_state(self, event):
        print("I'm entering sex state")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "讚數限制？(數字 or 隨意)")

    def on_enter_sex_limit_state(self, event):
        print("I'm entering sex limit state")
        sender_id = event['sender']['id']
        # url = pic_url("sex")
        responese = send_text_message(sender_id, "Sex limit~")
        # responese = send_text_message(sender_id, "From Dcard~")
        # responese = send_image_url(sender_id, url)
        self.go_back()

    def on_enter_sex_unlimit_state(self, event):
        print("I'm entering sex unlimit state")
        sender_id = event['sender']['id']
        url = pic_url("sex")
        responese = send_text_message(sender_id, "From Dcard~")
        responese = send_image_url(sender_id, url)
        self.go_back()

