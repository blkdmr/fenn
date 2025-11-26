class Notifier:
    def __init__(self):
        self.services = []

    def notify(self, message):
        for service in self.services:
            service.send_notification(message)