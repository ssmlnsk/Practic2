from database import Database


class Facade:
    """
    Класс фасада
    """
    def __init__(self):
        """
        Создание объекта БД
        """
        self.db = Database()

    def get_logins(self):
        """
        Получение списка логинов сотрудников
        :return: список логинов
        """
        return self.db.get_logins()

    def get_code_visiter(self, surname, name, lastName):
        """
        Получение кода и адреса клиента
        :param fio: ФИО
        :return: код и адрес клиента
        """
        return self.db.get_code_visiters(surname, name, lastName)

    def get_code_employees(self, surname, name, lastName):
        """
        Получение кода и адреса клиента
        :param fio: ФИО
        :return: код и адрес клиента
        """
        return self.db.get_code_employees(surname, name, lastName)

    def get_visiters(self):
        """
        Получение списка клиентов
        :return: Список клиентов
        """
        return self.db.get_visiters()

    def get_expositions(self):
        """
        Получение списка клиентов
        :return: Список клиентов
        """
        return self.db.get_expositions()

    def get_types_ticket(self):
        """
        Получение списка услуг
        :return: Список услуг
        """
        return self.db.get_types_ticket()

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
        """
        Получение кода услуги
        :param name: Наименование услуги
        :return: код услуги
        """
        return self.db.get_types_ticket_id(name)

    def get_id_visiter(self, surname, name, lastName):
        """
        Получение кода клиента
        :param fio:
        :return:
        """
        return self.db.get_visiter_id(surname, name, lastName)

    def get_code_exposition(self, exposition):
        """
        Получение кода клиента
        :param fio:
        :return:
        """
        return self.db.get_code_exposition(exposition)

    def get_for_authorization(self, login):
        """
        Получение информации о сотруднике
        :param login: Логин
        :return: password, role, last_exit, block, fio, photo
        """
        log = self.db.get_info(login)
        if log == []:
            return '', '', '', '', '', ''
        password, role, surname, name, lastname, photo = log[0], log[1], log[2], log[3], log[4], log[5]  # временные данные
        return password, role, surname, name, lastname, photo

    def insert_picture(self, name, year, painter, technic, type, photo):
        """
        Добавление услуги
        :param name: Наименование услуги
        :param code: Код услуги
        :param cost: Стоимость руб. за час
        :return: None
        """
        self.db.insert_picture(name, year, painter, technic, type, photo)

    def insert_painter(self, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style):
        """
        Добавление услуги
        :param name: Наименование услуги
        :param code: Код услуги
        :param cost: Стоимость руб. за час
        :return: None
        """
        self.db.insert_painter(surname, name, lastName, dateOfBirth, placeOfBirth, genre, style)

    def insert_exposition(self, theme, dateStart, dateEnd):
        """
        Добавление услуги
        :param name: Наименование услуги
        :param code: Код услуги
        :param cost: Стоимость руб. за час
        :return: None
        """
        self.db.insert_exposition(theme, dateStart, dateEnd)

    def delete_picture(self, id):
        """
        Удаление услуги
        :param id: id услуги
        :return: None
        """
        self.db.delete_picture(id)

    def delete_painter(self, id):
        """
        Удаление услуги
        :param id: id услуги
        :return: None
        """
        self.db.delete_painter(id)

    def delete_exposition(self, id):
        """
        Удаление услуги
        :param id: id услуги
        :return: None
        """
        self.db.delete_exposition(id)

    def update_picture(self, id, name, year, painter, technic, type, photo):
        """
        Обновление таблицы услуг
        :param id: id услуги
        :param name: Наименование услуги
        :param code: Код услуги
        :param cost: Стоимость руб. за час
        :return: None
        """
        self.db.update_picture(id, name, year, painter, technic, type, photo)

    def update_painter(self, id, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style):
        """
        Обновление таблицы услуг
        :param id: id услуги
        :param name: Наименование услуги
        :param code: Код услуги
        :param cost: Стоимость руб. за час
        :return: None
        """
        self.db.update_painter(id, surname, name, lastName, dateOfBirth, placeOfBirth, genre, style)

    def update_exposition(self, id, theme, dateStart, dateEnd):
        """
        Обновление таблицы услуг
        :param id: id услуги
        :param name: Наименование услуги
        :param code: Код услуги
        :param cost: Стоимость руб. за час
        :return: None
        """
        self.db.update_exposition(id, theme, dateStart, dateEnd)

    def create_ticket(self, number, date, type, exposition, visiter, employee, code):
        """
        Создание заказа
        :param number: Номер заказа
        :param date: Дата создания
        :param time: Время создания
        :param client: Код клиента
        :param service: Код услуги
        :return: None
        """
        self.db.insert_ticket(number, date, type, exposition, visiter, employee, code)

    def read_visiter(self):
        """
        Получение списка клиентов
        :return: Список клиентов
        """
        return self.db.select_visiters()

    def read_exposition(self):
        """
        Получение списка клиентов
        :return: Список клиентов
        """
        return self.db.select_exposition()

    def read_history(self):
        """
        Получение списка истории входа
        :return: список истории входа
        """
        return self.db.select_history()

    def insert_visiter(self, fio, passportData, dateOfBirth, address, email):
        """
        Добавление нового клиента
        :param fio: ФИО
        :param passportData: Паспортные данные
        :param dateOfBirth: Дата рождения
        :param address: Адрес
        :param email: E-mail
        :return: None
        """
        self.db.insert_visiter(fio, passportData, dateOfBirth, address, email)

    def read_pictures(self):
        """
        Получение списка услуг
        :return: Список услуг
        """
        return self.db.select_pictures()

    def read_painters(self):
        """
        Получение списка услуг
        :return: Список услуг
        """
        return self.db.select_painters()

    def insert_time_entry(self, login, time):
        """
        Добавление времени входа сотрудника
        :param login: Логин
        :param time: Дата и время
        :return: None
        """
        self.db.insert_time_entry(login, time)
