import mysql
from mysql.connector import connect


class Database:
    """
    Класс с функциями для взаимодействия с базой данных
    """
    def __init__(self):
        """
        Подключение к базе данных MySQL
        """
        self.conn = mysql.connector.connect(host='localhost', port=3306, user='root', database='artgallery')

    def insert_painter(self, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style):
        """
        Добавление новой услуги
        :param name: наименование услуги
        :param code: код услуги
        :param cost: стоимость руб. за час
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Художник VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)", (surname, name, lastName, dateOfBirth, placeOfBirth, genre, style))
        cursor.close()
        self.conn.commit()

    def insert_picture(self, name, year, painter, technic, type, photo):
        """
        Добавление новой услуги
        :param name: наименование услуги
        :param code: код услуги
        :param cost: стоимость руб. за час
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Картина VALUES (NULL, %s, %s, %s, %s, %s, %s)", (name, year, painter, technic, type, photo))
        cursor.close()
        self.conn.commit()

    def insert_exposition(self, theme, dateStart, dateEnd):
        """
        Добавление новой услуги
        :param name: наименование услуги
        :param code: код услуги
        :param cost: стоимость руб. за час
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO выставки VALUES (NULL, %s, %s, %s)", (theme, dateStart, dateEnd))
        cursor.close()
        self.conn.commit()

    def insert_ticket(self, number, date, type, exposition, visiter, employee, code):
        """
        Добавление нового заказа
        :param number: номер заказа
        :param date: дата создания
        :param time: время создания
        :param client: номер клиента
        :param service: услуги
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Билет VALUES (%s, %s, %s, %s, %s, %s, %s)", (number, date, type, exposition, visiter, employee, code))
        self.conn.commit()
        cursor.close()

    def update_picture(self, id, name, year, painter, technic, type, photo):
        """
        Обновление услуг
        :param id: id услуги
        :param name: наименование услуги
        :param code: код услуги
        :param cost: стоимость руб. за час
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE картина set `Название`='{name}', `Год написания`='{year}', `Код художника`='{painter}', `Код техники`='{technic}', `Код типа`='{type}', `Фото`='{photo}' WHERE `Код картины`='{id}'")
        self.conn.commit()
        cursor.close()

    def update_painter(self, id, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style):
        """
        Обновление услуг
        :param id: id услуги
        :param name: наименование услуги
        :param code: код услуги
        :param cost: стоимость руб. за час
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE художник set `Фамилия`='{surname}', `Имя`='{name}', `Отчество`='{lastName}', `Дата рождения`='{dateOfBirth}', `Место рождения`='{placeOfBirth}', `Жанр`='{genre}', `Стиль`='{style}' WHERE `Код художника`='{id}'")
        self.conn.commit()
        cursor.close()

    def update_exposition(self, id, theme, dateStart, dateEnd):
        """
        Обновление услуг
        :param id: id услуги
        :param name: наименование услуги
        :param code: код услуги
        :param cost: стоимость руб. за час
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE выставки set `Тема выставки`='{theme}', `Дата начала`='{dateStart}', `Дата окончания`='{dateEnd}' WHERE `Код выставки`='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_picture(self, id):
        """
        Удаление услуги
        :param id: id услуги
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM картина WHERE `Код картины`='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_painter(self, id):
        """
        Удаление услуги
        :param id: id услуги
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM художник WHERE `Код художника`='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_exposition(self, id):
        """
        Удаление услуги
        :param id: id услуги
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM выставки WHERE `Код выставки`='{id}'")
        self.conn.commit()
        cursor.close()

    def select_visiters(self):
        """
        Получение списка клиентов
        :return: rows
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM посетитель")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_employees(self):
        """
        Получение списка сотрудников
        :return: rows
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM сотрудник")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_pictures(self):
        """
        Получение списка услуг
        :return: rows
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM картина")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_painters(self):
        """
        Получение списка услуг
        :return: rows
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM художник")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_exposition(self):
        """
        Получение списка услуг
        :return: rows
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM выставки")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def get_info(self, login):
        """
        Получение информации о сотруднике
        :param login: логин сотрудника
        :return: log
        """
        log = []
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT Пароль, Должность, Фамилия, Имя, Отчество, Фото FROM сотрудник WHERE Логин = '{login}'""")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                log.append(j)
        return log
        cursor.close()

    def get_logins(self):
        """
        Получение списка логинов сотрудников
        :return: logins
        """
        logins = []
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT Логин FROM сотрудник""")
        rows = cursor.fetchall()

        for i in rows:
            for j in i:
                logins.append(j)
        return logins
        cursor.close()

    def get_code_visiters(self, surname, name, lastName):
        """
        Получение кода и адреса клиента
        :param fio: ФИО клиента
        :return: client
        """
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT `Код посетителя` FROM посетитель WHERE Фамилия='{surname}' and Имя='{name}' and Отчество='{lastName}'""")
        row = str(cursor.fetchone())
        return row
        cursor.close()

    def get_code_employees(self, surname, name, lastName):
        """
        Получение кода клиента
        :param fio: ФИО клиента
        :return: client
        """
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT `Код сотрудника` FROM сотрудник WHERE Фамилия='{surname}' and Имя='{name}' and Отчество='{lastName}'""")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_visiters(self):
        """
        Получение списка ФИО клиентов
        :return: clients
        """
        visiter = ''
        visiters = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Фамилия, Имя, Отчество FROM посетитель")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                visiter += j
                visiter += ' '
            visiters.append(visiter[0:-1])
            visiter = ''
        return visiters
        cursor.close()

    def get_expositions(self):
        """
        Получение списка ФИО клиентов
        :return: clients
        """
        expositions = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Тема выставки` FROM выставки")
        rows = cursor.fetchall()
        for i in rows:
            expositions.append(str(i)[2:-3])
        return expositions
        cursor.close()

    def get_id_expositions(self, name):
        """
        Получение списка ФИО клиентов
        :return: clients
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код выставки` FROM выставки WHERE `Тема выставки`='{name}")
        row = str(cursor.fetchone())
        return row
        cursor.close()

    def insert_visiter(self, lastName, name, surname, dateOfBirth, email):
        """
        Добавление нового клиента
        :param fio: ФИО
        :param passportData: Паспортные данные
        :param dateOfBirth: Дата рождения
        :param address: Адрес
        :param email: E-mail
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO посетитель VALUES (NULL, %s, %s, %s, %s, %s)", (lastName, name, surname, dateOfBirth, email))
        self.conn.commit()
        cursor.close()

    def get_types_ticket(self):
        """
        Получение списка наименований услуг
        :return: services
        """
        services = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Наименование категории` FROM категории")
        rows = cursor.fetchall()

        for i in rows:
            services.append(str(i)[2:-3])
        return services
        cursor.close()

    def get_types_ticket_id(self, name):
        """
        Получение кода услуги
        :param name: Наименование услуги
        :return: row
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код категории` FROM категории WHERE `Наименование категории`='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_painters(self):
        """
        Получение списка наименований услуг
        :return: services
        """
        painter = []
        painters = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Фамилия, Имя, Отчество FROM художник")
        rows = cursor.fetchall()
        for i in rows:
            for j in i:
                painter.append(j)
            painters.append(painter.copy())
            painter = []
        return painters
        cursor.close()

    def get_painter_id(self, surname, name, lastName):
        """
        Получение кода услуги
        :param name: Наименование услуги
        :return: row
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код художника` FROM художник WHERE Фамилия='{surname}' and Имя='{name}' and Отчество='{lastName}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_painter_id_without_lastName(self, surname, name):
        """
        Получение кода услуги
        :param name: Наименование услуги
        :return: row
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код художника` FROM художник WHERE Фамилия='{surname}' AND Имя='{name}';")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_technic(self):
        """
        Получение списка наименований услуг
        :return: services
        """
        services = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Техника FROM `техника картины`")
        rows = cursor.fetchall()

        for i in rows:
            services.append(str(i)[2:-3])
        return services
        cursor.close()

    def get_technic_id(self, name):
        """
        Получение кода услуги
        :param name: Наименование услуги
        :return: row
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код техники` FROM `техника картины` WHERE Техника='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_type(self):
        """
        Получение списка наименований услуг
        :return: services
        """
        services = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Тип FROM `Тип картины`")
        rows = cursor.fetchall()

        for i in rows:
            services.append(str(i)[2:-3])
        return services
        cursor.close()

    def get_type_id(self, name):
        """
        Получение кода услуги
        :param name: Наименование услуги
        :return: row
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код типа` FROM `тип картины` WHERE Тип='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_visiter_id(self, lastName, name, surname):
        """
        Получение кода клиента
        :param fio: ФИО
        :return: row
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код посетителя` FROM посетитель WHERE Фамилия='{lastName}' and Имя='{name}' and Отчество='{surname}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_code_exposition(self, exposition):
        """
        Получение кода клиента
        :param fio: ФИО
        :return: row
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код выставки` FROM выставки WHERE `Тема выставки`='{exposition}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def insert_time_entry(self, login, time):
        """
        Добавление времени входа сотрудника
        :param login: Логин
        :param time: Дата и время
        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(f"INSERT INTO `история входа` VALUES (NULL, %s, %s)", (time, login))
        self.conn.commit()
        cursor.close()

    def select_history(self):
        """
        Получение истории входа сотрудников
        :return:
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM `история входа`")
        rows = cursor.fetchall()
        return rows
        cursor.close()


if __name__ == '__main__':
    db = Database()
    print(db.get_types_ticket_id('Взрослый'))
