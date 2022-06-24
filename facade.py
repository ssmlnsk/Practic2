from database import Database


class Facade:
    def __init__(self):
        self.db = Database()

    def get_logins(self):
        return self.db.get_logins()

    def get_code_visiter(self, surname, name, lastName):
        return self.db.get_code_visiters(surname, name, lastName)

    def get_code_employees(self, surname, name, lastName):
        return self.db.get_code_employees(surname, name, lastName)

    def get_visiters(self):
        return self.db.get_visiters()

    def get_expositions(self):
        return self.db.get_expositions()

    def get_types_ticket(self):
        return self.db.get_types_ticket()

    def get_exhibited_picture(self):
        return self.db.get_exhibited_picture()

    def get_exhibited_picture_id(self, name):
        return self.db.get_exhibited_picture_id(name)

    def get_room(self):
        return self.db.get_room()

    def get_room_id(self, name):
        return self.db.get_room_id(name)

    def get_painters(self):
        return self.db.get_painters()

    def get_painters_id(self, surname, name, lastName):
        return self.db.get_painter_id(surname, name, lastName)

    def get_painter_id_without_lastName(self, surname, name):
        return self.db.get_painter_id_without_lastName(surname, name)

    def get_technic(self):
        return self.db.get_technic()

    def get_technic_id(self, technic):
        return self.db.get_technic_id(technic)

    def get_type(self):
        return self.db.get_type()

    def get_type_id(self, type):
        return self.db.get_type_id(type)

    def get_id_type_ticket(self, name):
        return self.db.get_types_ticket_id(name)

    def get_id_visiter(self, surname, name, lastName):
        return self.db.get_visiter_id(surname, name, lastName)

    def get_code_exposition(self, exposition):
        return self.db.get_code_exposition(exposition)

    def get_for_authorization(self, login):
        log = self.db.get_info(login)
        if log == []:
            return '', '', '', '', '', ''
        password, role, surname, name, lastname, photo = log[0], log[1], log[2], log[3], log[4], log[5]  # временные данные
        return password, role, surname, name, lastname, photo

    def insert_picture(self, name, year, painter, technic, type, photo):
        self.db.insert_picture(name, year, painter, technic, type, photo)

    def insert_painter(self, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style):
        self.db.insert_painter(surname, name, lastName, dateOfBirth, placeOfBirth, genre, style)

    def insert_exposition(self, theme, dateStart, dateEnd):
        self.db.insert_exposition(theme, dateStart, dateEnd)

    def insert_exhibited_picture(self, picture, exposition, room):
        self.db.insert_exhibited_picture(picture, exposition, room)

    def delete_picture(self, id):
        self.db.delete_picture(id)

    def delete_painter(self, id):
        self.db.delete_painter(id)

    def delete_exposition(self, id):
        self.db.delete_exposition(id)

    def delete_exhibited_picture(self, picture):
        self.db.delete_exhibited_picture(picture)

    def update_picture(self, id, name, year, painter, technic, type, photo):
        self.db.update_picture(id, name, year, painter, technic, type, photo)

    def update_painter(self, id, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style):
        self.db.update_painter(id, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style)

    def update_exposition(self, id, theme, dateStart, dateEnd):
        self.db.update_exposition(id, theme, dateStart, dateEnd)

    def update_exhibited_picture(self, picture, exposition, room):
        self.db.update_exhibited_picture(picture, exposition, room)

    def create_ticket(self, number, date, type, exposition, visiter, employee, code):
        self.db.insert_ticket(number, date, type, exposition, visiter, employee, code)

    def read_visiter(self):
        return self.db.select_visiters()

    def read_exposition(self):
        return self.db.select_exposition()

    def read_exhibited_picture(self):
        return self.db.select_exhibited_picture()

    def read_history(self):
        return self.db.select_history()

    def insert_visiter(self, surname, name, lastName, dateOfBirth, email):
        self.db.insert_visiter(surname, name, lastName, dateOfBirth, email)

    def read_pictures(self):
        return self.db.select_pictures()

    def read_painters(self):
        return self.db.select_painters()

    def insert_time_entry(self, login, time):
        self.db.insert_time_entry(login, time)

    def select_number_ticket(self):
        return self.db.select_number_ticket()
