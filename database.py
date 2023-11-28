class Database:
    def __init__(self):
        self.users = []
        self.appointments = []

    def save_user(self, user):
        self.users.append(user)

    def save_appointment(self, appointment):
        self.appointments.append(appointment)