from io import BytesIO

import barcode
from barcode import EAN13
from barcode.writer import ImageWriter
import img2pdf

from facade import Facade
import random

from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtWidgets
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer, QTime, QDateTime
from PyQt5.QtWidgets import QGraphicsScene, QListWidgetItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QDialog

import sys
import time
import datetime

import logging

from PyQt5.QtWidgets import QMessageBox

logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Отвечает за подключением к кнопкам, объявление переменных, заполнение таблиц,
        получение списка страниц StackedWidget
        """
        super().__init__()
        self.facade = Facade()
        self.ui = uic.loadUi("main.ui", self)

        self.page = self.ui.stackedWidget_main
        self.page_id = [0]  # тут будут индексы доступных страничек после авторизации для сотрудника
        self.now_page = 0

        self.page.setCurrentIndex(self.page_id[self.now_page])
        self.ui.btn_next.clicked.connect(self.next_page)
        self.ui.btn_back.clicked.connect(self.back_page)
        self.ui.btn_all_visiters.clicked.connect(self.page_all_visiters)
        self.ui.btn_exit.clicked.connect(self.exit)

        self.ui.btn_new_painter.clicked.connect(self.new_painter)
        self.ui.btn_delete_painter.clicked.connect(self.delete_painter)
        self.ui.btn_save_painters.clicked.connect(self.save_painters)

        self.ui.btn_new_exposition.clicked.connect(self.new_exposition)
        self.ui.btn_delete_exposition.clicked.connect(self.delete_exposition)
        self.ui.btn_save_exposition.clicked.connect(self.save_exposition)

        self.ui.btn_new_picture.clicked.connect(self.new_picture)
        self.ui.btn_delete_picture.clicked.connect(self.delete_picture)
        self.ui.btn_save_pictures.clicked.connect(self.save_pictures)

        self.build_combobox_visiters()
        self.build_combobox_type_ticket()
        self.build_combobox_expositions()

        self.ui.btn_new_ticket.clicked.connect(self.create_new_ticket)
        self.ui.btn_save_ticket.clicked.connect(self.save_ticket)

        self.ui.btn_new_visiter.clicked.connect(self.oped_new_visiter)

        self.updateTablePictures()
        self.updateTablePainters()
        self.updateTableExposition()
        self.updateTableHistory()

    def exit(self):
        """
        Отвечает за выход из программы
        :param block: блокировка
        :return:
        """
        self.now_page = 0
        self.page.setCurrentIndex(self.page_id[self.now_page])
        self.hide()
        self.open_auth()

    def page_all_visiters(self):
        """
        Отвечает за переход к странице с таблицей клиентов
        Обновление таблицы клиентов
        :return:
        """
        self.updateTableVisiters()
        self.page.setCurrentIndex(3)

    def updateTableVisiters(self):
        """
        Отвечает за обновление таблицы клиентов
        :return:
        """
        self.table_visiters.clear()
        rec = self.facade.read_visiter()
        self.ui.table_visiters.setColumnCount(6)
        self.ui.table_visiters.setRowCount(len(rec))
        self.ui.table_visiters.setHorizontalHeaderLabels(['Код посетителя', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Email'])

        for i, visiter in enumerate(rec):
            for x, field in enumerate(visiter):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_visiters.setItem(i, x, item)

    def updateTablePictures(self):
        """
        Отвечает за обновление таблицы услуг
        :return:
        """
        self.table_pictures.clear()
        rec = self.facade.read_pictures()
        self.ui.table_pictures.setColumnCount(7)
        self.ui.table_pictures.setRowCount(len(rec))
        self.ui.table_pictures.setHorizontalHeaderLabels(['ID', 'Название', 'Год написания', 'Художник', 'Техника', 'Тип', 'Фото'])

        for i, picture in enumerate(rec):
            for x, field in enumerate(picture):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_pictures.setItem(i, x, item)

    def updateTablePainters(self):
        """
        Отвечает за обновление таблицы услуг
        :return:
        """
        self.table_painters.clear()
        rec = self.facade.read_painters()
        self.ui.table_painters.setColumnCount(8)
        self.ui.table_painters.setRowCount(len(rec))
        self.ui.table_painters.setHorizontalHeaderLabels(['ID', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Место рождения', 'Жанр', 'Стиль'])

        for i, painter in enumerate(rec):
            for x, field in enumerate(painter):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_painters.setItem(i, x, item)

    def updateTableExposition(self):
        """
        Отвечает за обновление таблицы услуг
        :return:
        """
        self.table_exposition.clear()
        rec = self.facade.read_exposition()
        self.ui.table_exposition.setColumnCount(4)
        self.ui.table_exposition.setRowCount(len(rec))
        self.ui.table_exposition.setHorizontalHeaderLabels(['Код выставки', 'Тема выставки', 'Дата начала', 'Дата окончания'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_exposition.setItem(i, x, item)

    def updateTableHistory(self):
        """
        Отвечает за обновление таблицы истории входа
        :return:
        """
        self.table_entry.clear()
        rec = self.facade.read_history()
        self.table_entry.setColumnCount(5)
        self.table_entry.setRowCount(len(rec))
        self.table_entry.setHorizontalHeaderLabels(['ID', 'Время входа', 'Логин сотрудника'])

        for i, employee in enumerate(rec):
            for x, info in enumerate(employee):
                item = QTableWidgetItem()
                item.setText(str(info))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_entry.setItem(i, x, item)

    def new_exposition(self):
        """
        Создает и показывает диалоговое окно добавления новой картины.
        :return:
        """
        theme = self.ui.edit_theme.text()
        dateStart = self.ui.dateStart.dateTime().toString('yyyy-MM-dd')
        dateEnd = self.ui.dateEnd.dateTime().toString('yyyy-MM-dd')
        if theme != '':
            self.facade.insert_exposition(theme, dateStart, dateEnd)
        self.updateTableExposition()

    def delete_exposition(self):
        """
        Отвечает за удаление выбранной услуги
        :return:
        """
        SelectedRow = self.table_exposition.currentRow()
        rowcount = self.table_exposition.rowCount()
        colcount = self.table_exposition.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_exposition.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_exposition.model().index(-1, -1)
            self.table_exposition.setCurrentIndex(ix)

    def new_picture(self):
        """
        Создает и показывает диалоговое окно добавления новой картины.
        :return:
        """
        dialog_client = DialogNewPicture(self)
        dialog_client.setWindowTitle("Добавление новой картины")
        dialog_client.show()
        dialog_client.exec_()

    def delete_picture(self):
        """
        Отвечает за удаление выбранной услуги
        :return:
        """
        SelectedRow = self.table_pictures.currentRow()
        rowcount = self.table_pictures.rowCount()
        colcount = self.table_pictures.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_pictures.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_pictures.model().index(-1, -1)
            self.table_pictures.setCurrentIndex(ix)

    def new_painter(self):
        """
        Создает и показывает диалоговое окно добавления нового художника.
        :return:
        """
        dialog_client = DialogNewPainter(self)
        dialog_client.setWindowTitle("Добавление нового художника")
        dialog_client.show()
        dialog_client.exec_()

    def delete_painter(self):
        """
        Отвечает за удаление выбранной услуги
        :return:
        """
        SelectedRow = self.table_painters.currentRow()
        rowcount = self.table_painters.rowCount()
        colcount = self.table_painters.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_painters.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_painters.model().index(-1, -1)
            self.table_painters.setCurrentIndex(ix)

    def getFromTablePicture(self):
        """
        Получение данных из таблицы, чтобы потом записать их в БД
        :return: data
        """
        rows = self.table_pictures.rowCount()
        cols = self.table_pictures.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_pictures.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableExposition(self):
        """
        Получение данных из таблицы, чтобы потом записать их в БД
        :return: data
        """
        rows = self.table_exposition.rowCount()
        cols = self.table_exposition.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_exposition.item(row, col).text())
            data.append(tmp)
        return data

    def save_exposition(self):
        """
        Отвечает за сохранение данных об услугах в базу данных
        Обновление таблицы в интерфейсе
        :return:
        """
        data = self.getFromTableExposition()
        for string in data:
            if string[1] != '':
                self.facade.update_exposition(int(string[0]), string[1], string[2], string[3])
            else:
                self.facade.delete_exposition(int(string[0]))
        self.updateTableExposition()

    def getFromTablePainter(self):
        """
        Получение данных из таблицы, чтобы потом записать их в БД
        :return: data
        """
        rows = self.table_painters.rowCount()
        cols = self.table_painters.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_painters.item(row, col).text())
            data.append(tmp)
        return data

    def save_pictures(self):
        """
        Отвечает за сохранение данных об услугах в базу данных
        Обновление таблицы в интерфейсе
        :return:
        """
        data = self.getFromTablePicture()
        for string in data:
            if string[1] != '':
                self.facade.update_picture(int(string[0]), string[1], string[2], string[3], string[4], string[5], string[6])
            else:
                self.facade.delete_picture(int(string[0]))
        self.updateTablePictures()

    def save_painters(self):
        """
        Отвечает за сохранение данных об услугах в базу данных
        Обновление таблицы в интерфейсе
        :return:
        """
        data = self.getFromTablePainter()
        for string in data:
            if string[1] != '':
                self.facade.update_painter(int(string[0]), string[1], string[2], string[3], string[4], string[5], string[6], string[7])
            else:
                self.facade.delete_painter(int(string[0]))
        self.updateTablePainters()

    def build_combobox_visiters(self):
        """
        Добавление списка клиентов в ComboBox
        :return:
        """
        visiters = self.facade.get_visiters()
        self.comboBox_visiters.clear()
        if self.comboBox_visiters is not None:
            self.comboBox_visiters.addItems(visiters)
        logging.log(logging.INFO, 'ComboBox "Посетители" обновлён')

    def build_combobox_expositions(self):
        """
        Добавление списка клиентов в ComboBox
        :return:
        """
        expositions = self.facade.get_expositions()
        self.comboBox_expositions.clear()
        if self.comboBox_expositions is not None:
            self.comboBox_expositions.addItems(expositions)
        logging.log(logging.INFO, 'ComboBox "Выставки" обновлён')

    def build_combobox_type_ticket(self):
        """
        Добавление списка услуг в ComboBox
        :return:
        """
        types_ticket = self.facade.get_types_ticket()
        self.comboBox_type_ticket.clear()
        if self.comboBox_type_ticket is not None:
            self.comboBox_type_ticket.addItems(types_ticket)
        logging.log(logging.INFO, 'ComboBox "Категории" обновлён')

    def create_new_ticket(self):
        """
        Оформление нового заказа и его показ в ListWidget
        :return:
        """
        fio = self.comboBox_visiters.currentText().split()
        surname = fio[0]
        name = fio[1]
        lastName = fio[2]

        self.number_title = QListWidgetItem("Номер билета:")
        self.number = QListWidgetItem(str(self.facade.select_number_ticket()))
        self.date_visit_title = QListWidgetItem("Дата посещения:")
        self.date_visit = str(self.dateOfVisit.dateTime().toString('yyyy-MM-dd'))
        self.type_ticket_title = QListWidgetItem("Категория билета:")
        self.type_ticket = QListWidgetItem(self.comboBox_type_ticket.currentText())
        self.exposition_title = QListWidgetItem("Выставка:")
        self.exposition = QListWidgetItem(self.comboBox_expositions.currentText())
        self.visiter_title = QListWidgetItem("Посетитель:")
        self.visiter = QListWidgetItem(self.comboBox_visiters.currentText())
        self.visiter_code = QListWidgetItem(self.facade.get_code_visiter(surname, name, lastName))
        self.employee_title = QListWidgetItem("Сотрудник:")
        self.employee = QListWidgetItem(self.lbl_fio.text())
        self.add_new_ticket.clear()
        if self.number != 0:
            self.add_new_ticket.addItem(self.number_title)
            self.add_new_ticket.addItem(self.number)
            self.add_new_ticket.addItem(self.date_visit_title)
            self.add_new_ticket.addItem(self.date_visit)
            self.add_new_ticket.addItem(self.type_ticket_title)
            self.add_new_ticket.addItem(self.type_ticket)
            self.add_new_ticket.addItem(self.exposition_title)
            self.add_new_ticket.addItem(self.exposition)
            self.add_new_ticket.addItem(self.visiter_title)
            self.add_new_ticket.addItem(self.visiter)
            self.add_new_ticket.addItem(self.employee_title)
            self.add_new_ticket.addItem(self.employee)
        self.generateCode()

    def save_ticket(self):
        """
        Отвечает за сохранение заказа в базу данных
        :return:
        """
        ignore = [0, 2, 4, 6, 8, 10, 12]
        count = self.add_new_ticket.count()
        temp = [ind for ind in range(count) if ind not in ignore]
        ticket = []

        for i in temp:
            if i == 9:
                fio = str(self.add_new_ticket.item(i).text()).split()
                surname = fio[0]
                name = fio[1]
                lastName = fio[2]
                id_visiter = self.facade.get_id_visiter(surname, name, lastName)
                ticket.append(id_visiter)

            elif i == 5:
                type = str(self.add_new_ticket.item(i).text())
                id_type = self.facade.get_id_type_ticket(type)
                ticket.append(id_type)

            elif i == 7:
                exposition = str(self.add_new_ticket.item(i).text())
                id_exposition = self.facade.get_code_exposition(exposition)
                ticket.append(id_exposition)

            elif i == 11:
                fio = str(self.lbl_fio.text()).split()
                surname = fio[0]
                name = fio[1]
                lastName = fio[2]
                id_employee = self.facade.get_code_employees(surname, name, lastName)
                ticket.append(id_employee)

            else:
                ticket.append(self.add_new_ticket.item(i).text())

        temp = str(ticket[0] + ticket[1])
        number = temp.replace("-", "")

        self.facade.create_ticket(number, ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], str(self.name_code+'.png'))

    def generateCode(self):
        """
        Отвечает за создание штрих-кода по номеру, дате и времени заказа
        Создаётся в форматах .png и .pdf
        :return:
        """
        rv = BytesIO()
        EAN13 = barcode.get_barcode_class('code39')
        EAN13(str(100000902922), writer=ImageWriter()).write(rv)

        temp = str(self.facade.select_number_ticket()) + str(self.date_visit)
        temp_middle = temp.replace(".", "")
        temp_end = temp_middle.replace("-", "")

        self.name_code = "code" + temp_end

        with open("codes/" + self.name_code + '.png', "wb") as f:
            EAN13(temp_end, writer=ImageWriter(), add_checksum=False).write(f)

        a4_page_size = [img2pdf.in_to_pt(8.3), img2pdf.in_to_pt(11.7)]
        layout_function = img2pdf.get_layout_fun(a4_page_size)

        pdf = img2pdf.convert("codes/" + self.name_code + '.png', layout_fun=layout_function)
        with open("codes/" + self.name_code + '.pdf', 'wb') as f:
            f.write(pdf)

        icon = QtGui.QIcon('codes/' + self.name_code + '.png')
        item = QtWidgets.QListWidgetItem(icon, "")
        self.add_new_ticket.addItem(item)

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается при успешном создании кода.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Штрих-код")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()

    def next_page(self):
        """
        Отвечает за переход к следующей странице
        :return:
        """
        if self.now_page != len(self.page_id)-1:
            self.now_page += 1
            self.page.setCurrentIndex(self.page_id[self.now_page])

    def back_page(self):
        """
        Отвечает за переход к предыдущей странице
        :return:
        """
        if self.now_page != 0:
            self.now_page -= 1
            self.page.setCurrentIndex(self.page_id[self.now_page])

    def open_auth(self):
        """
        Создает и показывает диалоговое окно авторизации.
        Вызывается в __init__ и в функции exit
        :return:
        """
        dialog = DialogAuth(self)
        dialog.setWindowTitle("Авторизация")
        dialog.show()
        dialog.exec_()

    def oped_new_visiter(self):
        """
        Создает и показывает диалоговое окно создания нового клиента.
        :return:
        """
        dialog_visiter = DialogNewVisiter(self)
        dialog_visiter.setWindowTitle("Добавление нового клиента")
        dialog_visiter.show()
        dialog_visiter.exec_()


class DialogAuth(QDialog):
    def __init__(self, parent=None):
        """
        Отвечает за подключением к кнопкам, объявление переменных, создание сцены для «graphicsView»
        """
        super(DialogAuth, self).__init__(parent)
        self.ui = uic.loadUi("auth.ui", self)
        self.facade = Facade()

        self.scene = QGraphicsScene(0, 0, 300, 80)
        self.ui.draw_captcha.setScene(self.scene)
        self.ui.btn_enter.clicked.connect(self.enter)
        self.ui.btn_new_captcha.clicked.connect(self.captcha_generation)
        self.ui.btn_hide_password.clicked.connect(self.vis_pas)
        self.visible_captcha(False)

        self.count_try_entry = 0
        self.now_captcha = None
        self.next_try = 0
        self.vis_p = False

    def vis_pas(self):
        """
        Вызывается при нажатии на кнопку «btn_hide_password».
        Скрывает и показывает пароль (в соответствии с переменной self.vis_p)
        """
        ed = self.ui.edit_password
        if self.vis_p:
            self.vis_p = False
            ed.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.vis_p = True
            ed.setEchoMode(QtWidgets.QLineEdit.Normal)

    def visible_captcha(self, visible=True):
        """
        Вызывается в __init__ (с параметром False) и при второй неуспешной попытки входа
        (неправильный ввод пароля или логина) с параметом True.
        :param visible:
        При False скрывает поле ввода, кнопку обновления и сцену для отрисовки капчи
        При True - показывает поле ввода, кнопку обновления и сцену для отрисовки капчи
        """
        self.ui.draw_captcha.setVisible(visible)
        self.ui.edit_captcha.setVisible(visible)
        self.ui.label_4.setVisible(visible)
        self.ui.btn_new_captcha.setVisible(visible)

    def captcha_generation(self):
        """
        Вызывается при второй неуспешной попытке входа и при нажатии на кнопку «btn_new_captcha».
        Выводит капчу в «graphicsView» и возвращает значение капчи в переменной self.now_captcha
        """
        self.scene.clear()
        syms = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        count_syms = 3
        now_syms = ['']*count_syms
        x, y = 30, 20

        self.scene.addLine(0, random.randint(20, 45), 200, random.randint(30, 60))

        for i in range(count_syms):
            now_syms[i] = syms[random.randint(0, 35)]
            x+=20
            text = self.scene.addText(f"{now_syms[i]}")
            text.setFont(QFont("MS Shell Dlg 2", 15))
            text.moveBy(x, y+random.randint(-10, 20))
        self.now_captcha = ''.join(now_syms)

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается при неверном вводе пользователем логина, пароля, капчи.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Ошибка")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()

    def enter(self):
        """
        Вызывается при нажатии на кнопку btn_enter.
        Обрабатывает все случаи ввода данных (капчи, логина, пароля) и считает неуспешные попытки входа.
        Проверяет есть ли у пользователя блокировка и до скольки она длиться.
        При успешном входе передает в фасад время и логин успешного входа (для записи в бд),
        записывает индексы доступных страничек «Stacked Widget»
        (у разных сотрудников могут быть разные странички)
        """
        t = time.localtime()
        now_time = time.mktime(t)  # переводим в секунды
        auth_log = self.ui.edit_login.text()
        auth_pas = self.ui.edit_password.text()

        if auth_log == '' or auth_pas == '':
            logging.log(logging.INFO, 'Ошибка. Заполните все поля!')
            self.mes_box('Заполните все поля!')

        elif self.now_captcha is not None and self.ui.edit_captcha.text() == '':    # если капча существует и она не пустая
            logging.log(logging.INFO, 'Ошибка. Введите капчу!')
            self.mes_box('Введите капчу!')
        else:
            password, role, surname, name, lastname, photo = self.parent().facade.get_for_authorization(auth_log)
            pix = QPixmap(f'img/{photo}')

            if self.count_try_entry >= 3 and self.next_try > now_time:    # не прошло 10 секунд с прошлой попытки входа (после 3 неуспешной попытки)
                logging.log(logging.INFO, 'Ошибка. Подождите, прежде чем пытаться вводить снова.')
                self.mes_box('Подождите, прежде чем пытаться вводить снова.')
                return

            if self.now_captcha is not None and self.now_captcha != self.ui.edit_captcha.text():
                logging.log(logging.INFO, 'Ошибка. Неправильно введена капча.')
                self.mes_box('Неправильно введена капча.')
            elif password != auth_pas:    # неправильный пароль или вернул пустую строку тк нет такого логина
                self.count_try_entry += 1
                if self.count_try_entry >= 3:
                    self.next_try = now_time+10
                if password != '':  # если нет пароля, значит нет пользователя с введенным логином, поэтому записывать в историю входа не надо
                    time_entry = time.strftime("%d:%m:%Y %H:%M:%S", t)    # время неуспешной попытки входа
                    self.parent().facade.insert_time_entry(auth_log, time_entry)

                if self.count_try_entry == 2:
                    self.visible_captcha(True)
                    self.captcha_generation()
                    logging.log(logging.INFO, 'Ошибка. Вторая неуспешная попытка входа. Теперь введите капчу.')
                    self.mes_box('Вторая неуспешная попытка входа. Теперь введите капчу.')
                else:
                    logging.log(logging.INFO, 'Ошибка. Неправильно введены данные.')
                    self.mes_box('Неправильно введены данные.')
            elif password == auth_pas:
                time_entry = time.strftime("%Y-%m-%d %H:%M:%S", t)    # время успешной попытки входа
                self.parent().facade.insert_time_entry(auth_log, time_entry)
                logging.log(logging.INFO, 'Вход выполнен')
                fio = surname + ' ' + name + ' '+ lastname
                self.parent().surname_emp = surname
                self.parent().name_emp = name
                self.parent().lastname_emp = lastname
                self.parent().ui.lbl_fio.setText(fio)
                self.parent().ui.lbl_role.setText(role)
                if role == 'Страший экскурсовод' or role == 'Экскурсовод':
                    self.parent().hide()
                    self.parent().page_id = [0, 2]
                else:   # Администратор
                    self.parent().hide()
                    self.parent().page_id = [0, 1, 4, 5, 6, 7]
                self.parent().show()
                self.parent().ui.lbl_photo.setPixmap(pix)
                self.parent().now_login = auth_log
                self.close()


class DialogNewVisiter(QDialog):
    def __init__(self, parent=None):
        """
        Отвечает за подключение к кнопке "Добавить"
        """
        super(DialogNewVisiter, self).__init__(parent)
        self.ui = uic.loadUi("new_visiter.ui", self)
        self.facade = Facade()

        self.ui.btn_add_visiter.clicked.connect(self.add)

    def add(self):
        """
        Отвечает за добавление клиента в базу данных
        :return:
        """
        self.surname = self.ui.edit_surname.text()
        self.name = self.ui.edit_name.text()
        self.lastName = self.ui.edit_lastName.text()
        self.dateOfBirth = self.ui.date_birth.dateTime().toString('yyyy-MM-dd')
        self.email = self.ui.edit_email.text()

        if self.surname != '' and self.name != '' and self.lastName != '' and self.dateOfBirth != '' and self.email != '':
            self.facade.insert_visiter(self.surname, self.name, self.lastName, self.dateOfBirth, self.email)
        else:
            self.mes_box('Заполните все поля!')

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается, если какое-либо поле не заполнено.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Ошибка")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()


class DialogNewPicture(QDialog):
    def __init__(self, parent=None):
        """
        Отвечает за подключение к кнопке "Добавить"
        """
        super(DialogNewPicture, self).__init__(parent)
        self.ui = uic.loadUi("new_picture.ui", self)
        self.facade = Facade()

        self.ui.btn_add_client.clicked.connect(self.add)

        self.build_combobox_painter()
        self.build_combobox_technic()
        self.build_combobox_type()

    def add(self):
        """
        Отвечает за добавление клиента в базу данных
        :return:
        """
        self.name = self.ui.edit_name.text()
        self.year = self.ui.edit_year.text()
        self.painter = self.ui.combobox_painter.currentText()
        self.technic = self.ui.combobox_technic.currentText()
        self.type = self.ui.combobox_type.currentText()
        self.photo = self.ui.edit_photo.text()

        if self.name != '' and self.year != '' and self.painter != '' and self.technic != '' and self.type != '' and self.photo != '':
            fio = self.painter.split(', ')
            surname = fio[0]
            name = fio[1]
            if len(fio) == 2:
                painter = self.facade.get_painter_id_without_lastName(surname, name)
            else:
                lastName = fio[2]
                painter = self.facade.get_painters_id(surname, name, lastName)
            technic = self.facade.get_technic_id(self.technic)
            type = self.facade.get_type_id(self.type)
            self.facade.insert_picture(self.name, self.year, painter, technic, type, self.photo)
            self.parent.updateTablePictures()
        else:
            self.mes_box('Заполните все поля!')

    def build_combobox_painter(self):
        """
        Добавление списка услуг в ComboBox
        :return:
        """
        painters = []
        temp = ''
        painter = self.facade.get_painters()
        for i in painter:
            for x, j in enumerate(i):
                if j != '':
                    temp += j
                    temp += ', '
                else:
                    continue
            painters.append(temp[0:-2])
            temp = ''
        self.combobox_painter.clear()
        if self.combobox_painter is not None:
            self.combobox_painter.addItems(painters)
        logging.log(logging.INFO, 'ComboBox "Категории" обновлён')

    def build_combobox_technic(self):
        """
        Добавление списка услуг в ComboBox
        :return:
        """
        technic = self.facade.get_technic()
        self.combobox_technic.clear()
        if self.combobox_technic is not None:
            self.combobox_technic.addItems(technic)
        logging.log(logging.INFO, 'ComboBox "Категории" обновлён')

    def build_combobox_type(self):
        """
        Добавление списка услуг в ComboBox
        :return:
        """
        type = self.facade.get_type()
        self.combobox_type.clear()
        if self.combobox_type is not None:
            self.combobox_type.addItems(type)
        logging.log(logging.INFO, 'ComboBox "Категории" обновлён')

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается, если какое-либо поле не заполнено.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Ошибка")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()


class DialogNewPainter(QDialog):
    def __init__(self, parent=None):
        """
        Отвечает за подключение к кнопке "Добавить"
        """
        super(DialogNewPainter, self).__init__(parent)
        self.ui = uic.loadUi("new_painter.ui", self)
        self.facade = Facade()

        self.ui.btn_add_painter.clicked.connect(self.add)

    def add(self):
        """
        Отвечает за добавление клиента в базу данных
        :return:
        """
        self.surname = self.ui.edit_surname.text()
        self.name = self.ui.edit_name.text()
        self.lastName = self.ui.edit_lastName.text()
        self.dateOfBirth = self.ui.date_birth.dateTime().toString('yyyy-MM-dd')
        self.placeOfBirth = self.ui.place_birth.text()
        self.genre = self.ui.edit_genre.text()
        self.style = self.ui.edit_style.text()

        if self.surname != '' and self.name != '' and self.lastName != '' and self.dateOfBirth != '' and self.placeOfBirth != '' and self.genre != '' and self.style != '':
            self.facade.insert_painter(self.surname, self.name, self.lastName, self.dateOfBirth, self.placeOfBirth, self.genre, self.style)
        else:
            self.mes_box('Заполните все поля!')

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается, если какое-либо поле не заполнено.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Ошибка")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()


class Builder:
    """
    Паттерн строитель.
    Это порождающий паттерн проектирования, который позволяет создавать сложные объекты пошагово.
    """
    def __init__(self):
        self.qapp = QApplication(sys.argv)
        self.window = MainWindow()
        self.auth()

    def auth(self):
        self.window.open_auth()
        self.qapp.exec()


if __name__ == '__main__':
    B = Builder()
