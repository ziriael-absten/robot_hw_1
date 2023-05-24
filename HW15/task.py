class Bot:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(message)
    def say_name(self):
        print(self.name)

# task2

class TelegramBot(Bot):

    def __init__(self, name, url=None, chat_id=None):
        self.chat_id = chat_id
        self.url = url
        super().__init__(name)

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"{message}, {self.url}, {self.chat_id}")



