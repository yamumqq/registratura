import sqlite3



class DoctorsDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('doctors.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS doctors
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           position TEXT NOT NULL,
                           doctor TEXT NOT NULL,
                        cabinet INTEGER NOT NULL)''')

        cursor.execute("INSERT INTO doctors (position, doctor,cabinet) VALUES (?, ?, ?)",
                       ('ЛОР', 'Сергей Богданович Дудко', 105))
        cursor.execute("INSERT INTO doctors (position, doctor,cabinet) VALUES (?, ?, ?)",
                       ('Дежурный врач', 'Данила Александрович Мраченко', 203))

        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           username TEXT NOT NULL,
                           password TEXT NOT NULL,
                           role TEXT NOT NULL)''')
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                        ('Danila', '12345', 'doctor'))
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                        ('admin', 'admin123', 'admin'))

        self.connection.commit()

    def validate_user(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            return user[3] 
        else:
            return None

    def get_doctors(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM doctors")
        return cursor.fetchall()

    def add_doctor(self, position, doctor,cabinet):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO doctors (position, doctor,cabinet) VALUES (?, ?, ?)",
                       (position, doctor,cabinet))
        self.connection.commit()

    def update__password_admin(self, password, name):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (password, name))
        self.connection.commit()
    def update__name_admin(self, new_name, name):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE users SET name = ? WHERE username = ?", (new_name, name))
        self.connection.commit()
    def update_user_name(self, name, new_name):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE users SET name = ? WHERE username = ?", (new_name, name))
        self.connection.commit()
    def update_doctorcabinet(self, doctor_id, newcabinet):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE doctors SETcabinet = ? WHERE id = ?", (newcabinet, doctor_id))
        self.connection.commit()
    def delete_doctors(self,doctor_ids):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM doctors WHERE id >0",(doctor_ids))
        self.connection.commit()
    def delete_doctor(self, doctor_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM doctors WHERE id = ?", (doctor_id,))
        self.connection.commit()


class doctor:
    def __init__(self, position, doctor, cabinet):
        self.position = position
        self.doctor = doctor
        self.cabinet = cabinet

    def __str__(self):
        return f"{self.position} - {self.doctor} ({self.cabinet} шт.)"


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class doctors:
    def __init__(self, database):
        self.database = database
        self.current_user = User('','','')

    def login(self, username, password):
        role = self.database.validate_user(username, password)
        if role:
            self.current_user = User(username, password, role)
            print('Авторизация успешна.')
        else:
            print('Ошибка авторизации.')


    def change_password_admin(self, new_password, name):
        if self.current_user.role == 'admin':
            self.database.update__password_admin(new_password, name)
            print('Доктор добавлен в больницу.')
        else:
            print('Ошибка доступа. Добавлять докторов может только администратор.')

    def add_doctor(self, position, doctor,cabinet):
        if self.current_user.role == 'admin':
            self.database.add_doctor(position, doctor,cabinet)
            print('Доктор добавлен в больницу.')
        else:
            print('Ошибка доступа. докторов может только администратор.')

    def delete_doctors(self,doctor_ids):
            self.database.delete_doctors(doctor_ids)
            print('Доктор успешно удален из больницы.')


    def delete_doctor(self, doctor_id):
        if self.current_user.role == 'admin':
            self.database.delete_doctor(doctor_id)
            print('Доктор успешно удален из больницы.')
        else:
            print('Ошибка доступа. Удалять докторов может только администратор.')

    def show_doctors(self):
        doctors = self.database.get_doctors()
        for doctor in doctors:
            doctor_obj = doctor(doctor[1], doctor[2], doctor[3])
            print(doctor_obj)

    def update_doctorcabinet(self, doctor_id, newcabinet):
        if self.current_user.role == 'admin':
            self.database.update_doctorcabinet(doctor_id, newcabinet)
            print('Количество докторов успешно обновлено.')
        else:
            print('Ошибка доступа. Обновлять количество докторов может только администратор.')


database = DoctorsDatabase()

c = 2
doctor_ids = 0
doctors = doctors(database)
print("Введите ваше имя пользователя:")
name = input()
print("Введите ваш пароль:")
passward = input()
doctors.login(name, passward)
while True:
    if(name == "admin"):
        print("Что вы хотите сделать?")
        print("1. Изменить свое имя")
        print("2. Изменить пароль пользователя")
        print("3. Удалить доктора из больницы")
        print("4. Добавить доктора в больницу")
        print("5. Выйти")


        answer = input("Введите номер команды: ")
        match answer:
            case "1":
                print("Введите новый пароль")
                new_passward = input()
                doctors.change_password_admin(new_passward,name)
            case "2":  
                continue
            case "3":
                for i in range(c,doctor_ids):
                    doctors.delete_doctors(i)
                continue
            case "4":
                doctors.add_doctor('Педиатр', 'Владлен Иванович Ключник', 108)
                c=c+1
                doctor_ids = c
                continue
            case "5":
                for i in range(c,doctor_ids):
                    doctors.delete_doctors(i)
                break
            case _:
                print("Такой команды нету!")
    
    doctors.show_doctors()


    doctors.update_doctorcabinet(1, 8)


    doctors.delete_doctor(2)