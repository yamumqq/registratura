from abc import ABC, abstractmethod

class Doctor(ABC):
    def __init__(self, username, password, doctor_info):
        self.username = username
        self.password = password
        self.doctor_info = doctor_info

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def login(self):
        pass