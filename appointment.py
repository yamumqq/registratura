class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def schedule_appointment(self):
        print(f"Запись на прием назначена на {self.date} у доктора {self.doctor.username} для пациента {self.patient.username}.")