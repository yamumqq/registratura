from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, username, password, patient_info):
        self.username = username
        self.password = password
        self.patient_info = patient_info

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def login(self):
        pass