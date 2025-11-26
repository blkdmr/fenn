from abc import ABC, abstractmethod
import requests

class Service(ABC):
    @abstractmethod
    def send_notification(self,message):
        pass
