from patient import Patient
from doctor import Doctor
from admin import Admin
from appointment import Appointment
from database import Database

class RegistrationSystem:
    def __init__(self, database):
        self.database = database

    def register_user(self, user):
        try:
            user.register()
            self.database.save_user(user)
        except Exception as e:
            print(f"Ошибка при регистрации: {str(e)}")
            print("Регистрация не удалась. Пожалуйста, повторите попытку.")

    def login_user(self, username, password):
        try:
            for user in self.database.users:
                if user.username == username and user.password == password:
                    user.login()
                    return True
            print("Вход не выполнен. Пользователь не найден.")
            return False
        except Exception as e:
            print(f"Ошибка при входе: {str(e)}")
            print("Вход не выполнен. Пожалуйста, повторите попытку.")

    def display_user_info(self):
        for user in self.database.users:
            print(f"Имя пользователя: {user.username}")
            print(f"Роль: {type(user).__name__}")
            if isinstance(user, Patient):
                print(f"Информация о пациенте: {user.patient_info}")
            elif isinstance(user, Doctor):
                print(f"Информация о враче: {user.doctor_info}")
            elif isinstance(user, Admin):
                print(f"Информация об администраторе: {user.admin_info}")
            print("=" * 20)