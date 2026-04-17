from data_manager import *
from twilio.rest import Client


dotenv.load_dotenv()


class Notifier:
    def __init__(self):
        self.client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
        self.my_number = os.getenv('MY_NUMBER')
        self.twilio_number = os.getenv('TWILIO_NUMBER')


    def send_notification(self, show_id):
        data_manager = DataManager()
        show_name, row_id = data_manager.find_episode_by_id(show_id)
        message = self.client.messages.create(
            body=f"Show on tonight!\nShow name: {show_name}",
            from_=self.twilio_number,
            to=self.my_number,
        )