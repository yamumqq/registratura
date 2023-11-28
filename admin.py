from abc import ABC, abstractmethod

class Admin(ABC):
    def __init__(self, username, password, admin_info):
        self.username = username
        self.password = password
        self.admin_info = admin_info

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def login(self):
        pass