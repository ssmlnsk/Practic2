import mysql
from mysql.connector import connect


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', port=3306, user='root', database='artgallery')

    def insert_painter(self, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Художник VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)", (surname, name, lastName, dateOfBirth, placeOfBirth, genre, style))
        cursor.close()
        self.conn.commit()

    def insert_picture(self, name, year, painter, technic, type, photo):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Картина VALUES (NULL, %s, %s, %s, %s, %s, %s)", (name, year, painter, technic, type, photo))
        cursor.close()
        self.conn.commit()

    def insert_exposition(self, theme, dateStart, dateEnd):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO выставки VALUES (NULL, %s, %s, %s)", (theme, dateStart, dateEnd))
        cursor.close()
        self.conn.commit()

    def insert_ticket(self, number, date, type, exposition, visiter, employee, code):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Билет VALUES (%s, %s, %s, %s, %s, %s, %s)", (number, date, type, exposition, visiter, employee, code))
        self.conn.commit()
        cursor.close()

    def insert_exhibited_picture(self, picture, exposition, room):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO `выставленные картины` VALUES (%s, %s, %s)", (picture, exposition, room))
        self.conn.commit()
        cursor.close()

    def update_picture(self, id, name, year, painter, technic, type, photo):
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE картина set `Название`='{name}', `Год написания`='{year}', `Код художника`='{painter}', `Код техники`='{technic}', `Код типа`='{type}', `Фото`='{photo}' WHERE `Код картины`='{id}'")
        self.conn.commit()
        cursor.close()

    def update_painter(self, id, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style):
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE художник set `Фамилия`='{surname}', `Имя`='{name}', `Отчество`='{lastName}', `Дата рождения`='{dateOfBirth}', `Место рождения`='{placeOfBirth}', `Жанр`='{genre}', `Стиль`='{style}' WHERE `Код художника`='{id}'")
        self.conn.commit()
        cursor.close()

    def update_exposition(self, id, theme, dateStart, dateEnd):
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE выставки set `Тема выставки`='{theme}', `Дата начала`='{dateStart}', `Дата окончания`='{dateEnd}' WHERE `Код выставки`='{id}'")
        self.conn.commit()
        cursor.close()

    def update_exhibited_picture(self, picture, exposition, room):
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE `выставленные картины` set `Код выставки`='{exposition}', `Код зала`='{room}' WHERE `Код картины`='{picture}'")
        self.conn.commit()
        cursor.close()

    def delete_picture(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM картина WHERE `Код картины`='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_painter(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM художник WHERE `Код художника`='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_exposition(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM выставки WHERE `Код выставки`='{id}'")
        self.conn.commit()
        cursor.close()

    def delete_exhibited_picture(self, picture):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM `выставленные картины` WHERE `Код картины`='{picture}'")
        self.conn.commit()
        cursor.close()

    def select_visiters(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM посетитель")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_employees(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM сотрудник")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_pictures(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM картина")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_painters(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM художник")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_exposition(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM выставки")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_exhibited_picture(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM `выставленные картины`")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def get_info(self, login):
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
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT `Код посетителя` FROM посетитель WHERE Фамилия='{surname}' and Имя='{name}' and Отчество='{lastName}'""")
        row = str(cursor.fetchone())
        return row
        cursor.close()

    def get_code_employees(self, surname, name, lastName):
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT `Код сотрудника` FROM сотрудник WHERE Фамилия='{surname}' and Имя='{name}' and Отчество='{lastName}'""")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_visiters(self):
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
        expositions = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Тема выставки` FROM выставки")
        rows = cursor.fetchall()
        for i in rows:
            expositions.append(str(i)[2:-3])
        return expositions
        cursor.close()

    def get_id_expositions(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код выставки` FROM выставки WHERE `Тема выставки`='{name}")
        row = str(cursor.fetchone())
        return row
        cursor.close()

    def insert_visiter(self, surname, name, lastName, dateOfBirth, email):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO посетитель VALUES (NULL, %s, %s, %s, %s, %s)", (surname, name, lastName, dateOfBirth, email))
        self.conn.commit()
        cursor.close()

    def get_exhibited_picture(self):
        exhibited_pictures = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Название FROM картина")
        rows = cursor.fetchall()

        for i in rows:
            exhibited_pictures.append(str(i)[2:-3])
        return exhibited_pictures
        cursor.close()

    def get_exhibited_picture_id(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код картины` FROM картина WHERE Название='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_room(self):
        rooms = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Наименование зала` FROM зал")
        rows = cursor.fetchall()
        for i in rows:
            rooms.append(str(i)[2:-3])
        return rooms
        cursor.close()

    def get_room_id(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код зала` FROM зал WHERE `Наименование зала`='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_types_ticket(self):
        types_ticket = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Наименование категории` FROM категории")
        rows = cursor.fetchall()

        for i in rows:
            types_ticket.append(str(i)[2:-3])
        return types_ticket
        cursor.close()

    def get_types_ticket_id(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код категории` FROM категории WHERE `Наименование категории`='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_painters(self):
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
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код художника` FROM художник WHERE Фамилия='{surname}' and Имя='{name}' and Отчество='{lastName}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_painter_id_without_lastName(self, surname, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код художника` FROM художник WHERE Фамилия='{surname}' AND Имя='{name}';")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_technic(self):
        services = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Техника FROM `техника картины`")
        rows = cursor.fetchall()

        for i in rows:
            services.append(str(i)[2:-3])
        return services
        cursor.close()

    def get_technic_id(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код техники` FROM `техника картины` WHERE Техника='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_type(self):
        services = []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT Тип FROM `Тип картины`")
        rows = cursor.fetchall()

        for i in rows:
            services.append(str(i)[2:-3])
        return services
        cursor.close()

    def get_type_id(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код типа` FROM `тип картины` WHERE Тип='{name}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_visiter_id(self, lastName, name, surname):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код посетителя` FROM посетитель WHERE Фамилия='{lastName}' and Имя='{name}' and Отчество='{surname}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def get_code_exposition(self, exposition):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Код выставки` FROM выставки WHERE `Тема выставки`='{exposition}'")
        row = str(cursor.fetchone())
        return row[1:-2]
        cursor.close()

    def insert_time_entry(self, login, time):
        cursor = self.conn.cursor()
        cursor.execute(f"INSERT INTO `история входа` VALUES (NULL, %s, %s)", (time, login))
        self.conn.commit()
        cursor.close()

    def select_history(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT `Время входа`, `Логин` FROM `история входа`")
        rows = cursor.fetchall()
        return rows
        cursor.close()

    def select_number_ticket(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT MAX(`Код билета`) FROM Билет")
        rows = cursor.fetchone()
        for i in rows:
            temp = str(i)[0:-8]
            i = int(temp) + 1
            return i
        cursor.close()
