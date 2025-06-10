from PyQt6 import QtWidgets, QtCore

from profile_1 import *
from calendar1 import *
from cabinetui import *
from login import *
from reg import *
from admin import *

from datetime import datetime, date
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QRadioButton,
    QComboBox,
    QCheckBox,
    QLineEdit,
    QLabel,
    QPushButton,
    QSpacerItem,
    QSizePolicy,
    QButtonGroup,
    QDialog,
)
import sys
import MySQLdb as mdb

db = mdb.connect(
    host="localhost",
    user="root",
    password="",
    database="TROPIK",
    port=3306,
)


class sqlconnect:
    def selectall(self):
        cur = db.cursor()
        otvet = cur.execute("select * from users")
        data = cur.fetchall()
        print("Вся инфа")
        for row in data:
            print(row)
        cur.close()
        return data

    def select_cabs(self):
        cur = db.cursor()
        otvet = cur.execute("select * from cabinets WHERE busy = 0")
        data = cur.fetchall()
        print("кабы")
        cur.close()
        return data

    def select_res(self):
        cur = db.cursor()
        otvet = cur.execute("select * from resuorses WHERE busy = 0")
        data = cur.fetchall()
        print("ресы")
        cur.close()
        return data

    def sel_orders_history(self, info):
        cur = db.cursor()
        otvet = cur.execute(f"SELECT * from orders where teacher_id = {info}")
        data = cur.fetchall()
        print("история заявок")
        cur.close()
        return data

    def sel_last_order(self):
        cur = db.cursor()
        otvet = cur.execute(f"SELECT * FROM orders ORDER BY id DESC LIMIT 1")
        data = cur.fetchall()
        print("последняя заявка")
        cur.close()
        return data


info = {
    "id_user": 1,  # Обычно None
    "date_para": None,
    "num_para": None,
    "num_cab": None,
    "technik": None,
    "login": None,
    "password": None,
}
info_user = info["id_user"]


class Profilek(QtWidgets.QWidget, Pro_Ui_Form):
    def __init__(
        self,
        login: str,
        pwd: str,
        parent=None,
    ):
        super().__init__(parent)
        self.setupUi(self)
        self.login = login
        self.pwd = pwd
        self.get_username()

        self.zapoln_combo()
        # self.status_text()+
        self.pushButton_2.clicked.connect(self.create_order)
        self.exitpushButton.clicked.connect(self.go_to_login)

        self.historycomboBox.currentIndexChanged.connect(self.change_status)

    def change_status(self):
        (
            self.statuslineEdit.setText("Одобрена")
            if self.historycomboBox.currentText().split()[4] == "1"
            else self.statuslineEdit.setText("В рассмотрении")
        )

    def go_to_login(self):
        self.log_in = Login_Window()
        self.log_in.show()
        self.close()

    def get_username(self):
        cur = db.cursor()
        res = cur.execute(f"SELECT login FROM users WHERE login = '{self.login}'")
        username = list(cur.fetchone())
        cur.close()
        self.lastnamelineEdit.setText(f"{username[0]}")
        self.lastnamelineEdit.setEnabled(False)

    def create_order(self):
        self.create_orders = Calendarik()
        self.create_orders.show()
        self.close()

    # ОКНО СТАТУС ДОДЕЛАТЬ!!!!!!!!!!!!!!!
    def status_text(self):
        last_order = sqlconnect().sel_last_order()
        self.statuslineEdit.setText(str(last_order[-1]))

    def zapoln_combo(self):
        try:

            orders = sqlconnect().sel_orders_history(info["id_user"])
            self.historycomboBox.clear()

            for row in orders:
                slovo = f"{str(row[0])} {str(row[2])} {str(row[3])} {str(row[4])} {str(row[5])}"
                self.historycomboBox.addItem(slovo)

        except Exception as e:
            print(f"Ошибка при заполнении комбобокса: {e}")
            # Можно добавить QMessageBox с ошибкой

        self.pushButton_2.clicked.connect(self.new_btn_order)

    def new_btn_order(self):
        self.cali_window = Calendarik()
        self.cali_window.show()
        self.close()


class Cabinetik(QtWidgets.QWidget, Cabi_Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        otvet1 = sqlconnect().select_cabs()
        for row in otvet1:
            item = QtWidgets.QListWidgetItem(str(row[1]))  # Отображаем только номер
            item.setData(QtCore.Qt.ItemDataRole.UserRole, row[0])  # Сохраняем ID
            self.cabinetlistWidget.addItem(item)

        # Загрузка ресурсов
        otvet2 = sqlconnect().select_res()
        for row in otvet2:
            item = QtWidgets.QListWidgetItem(str(row[1]))  # Отображаем только название
            item.setData(QtCore.Qt.ItemDataRole.UserRole, row[0])  # Сохраняем ID
            self.listWidget_2.addItem(item)

        # Кнопка отправить на проверку
        self.send_pushButton.clicked.connect(self.sender1)

        self.datalineEdit.setText(info["date_para"])
        self.paralineEdit.setText(str(info["num_para"]))
        # Кнопка назад
        self.back_btn.clicked.connect(self.back_button)

    def sender1(self):
        try:
            current_cab = self.cab.text()
            current_tech = self.tech.text()
            # info["num_cab"] = current_cab
            # info["technik"] = current_tech
            info["num_cab"] = self.cab_id
            info["technik"] = self.res_id
            print(info)
            cur = db.cursor()
            cur.execute(
                f"INSERT INTO orders (teacher_id, cabinet_id, resourse_id, date_of_order) VALUES ('{info['id_user']}', '{info['num_cab']}', '{info['technik']}', '{info['date_para']}')"
            )
            cur.close()
            db.commit()
            self.profi_wind = Profilek(login=info["login"], pwd=info["password"])
            self.profi_wind.show()
            self.close()

        except Exception as e:
            print(f"Ошибка - {e}")
            error_message = QLabel(self)
            error_message.setText("Заполните все поля!")
            error_message.move(160, 250)
            error_message.adjustSize()
            error_message.show()

    def back_button(self):
        self.cali_window = Calendarik()
        self.cali_window.show()
        self.close()


class Calendarik(QtWidgets.QWidget, Cal_Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.next_pushButton.clicked.connect(self.open_cabinet)
        self.pushButton_2.clicked.connect(self.open_profile)

    def open_profile(self):
        self.open_prof = Profilek(login=info["login"], pwd=info["password"])
        self.open_prof.show()
        self.close()

    def open_cabinet(self):
        try:
            if not hasattr(self, "selected_date") or self.selected_date is None:
                raise ValueError("Дата не выбрана")
            if not hasattr(self, "selected_para") or self.selected_para is None:
                raise ValueError("Номер пары не выбран")
            current_date = self.selected_date
            current_para = self.selected_para

            date_str = current_date.toString("yyyy-MM-dd")  # "dd.MM.yyyy"
            info["num_para"] = current_para
            info["date_para"] = date_str

            print(f"Дата: {date_str}, Пара: {current_para}")
            print(info)

            self.cabi_window = Cabinetik()
            self.cabi_window.show()
            self.close()
        except Exception as e:
            print(f"Ошибка - {e}")
            error_message = QLabel(self)
            error_message.setText("Заполните все поля!")
            error_message.move(250, 260)
            error_message.adjustSize()
            error_message.show()


class Reg_Win(QtWidgets.QWidget, Reg_window_Ui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.open_login)
        self.pushButton.clicked.connect(self.register_user)

    def register_user(self):
        le1 = self.lineEdit.text()
        le2 = self.lineEdit_2.text()
        curr = db.cursor()
        curr.execute(f"SELECT * FROM users WHERE login = '{le1}'")
        exist = curr.fetchone()
        curr.close()

        if (
            len(le1) < 20
            and le1 not in ["+", "(", ")", "'", "^", ";", ":", "%", "$", "#", "@", "!"]
            and len(le2) < 20
            and le2 not in ["+", "(", ")", "'", "^", ";", ":", "%", "$", "#", "@", "!"]
            and exist is None
            and le1 != ""
        ):
            cur = db.cursor()
            cur.execute(
                f"INSERT INTO `users` (`id`, `login`, `pass`) VALUES (NULL, '{le1}', '{le2}');"
            )
            cur.close()
            db.commit()
            cur = db.cursor()
            cur.execute(
                f"SELECT id, login, pass FROM users WHERE login = '{le1}' and pass = '{le2}'"
            )
            res = list(cur.fetchone())
            info["id_user"] = res[0]
            info["login"] = res[1]
            info["password"] = res[2]
            self.profilec = Profilek(login=le1, pwd=le2)
            self.profilec.show()
            self.close()
        else:
            self.error_message = QLabel(self)
            self.error_message.setText("Недопустимый логин или пароль")
            self.error_message.move(70, 170)
            self.error_message.adjustSize()
            self.error_message.show()

    def open_login(self):
        self.log_win = Login_Window()
        self.log_win.show()
        self.close()


class Admin_Form(QtWidgets.QWidget, Admin_Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.loaddata()

        self.pushButton_3.clicked.connect(self.go_to_login)
        self.pushButton.clicked.connect(self.odobrit)
        self.pushButton_2.clicked.connect(self.otclonit)

    def otclonit(self):
        cur_row = self.tableWidget.currentRow()
        self.tableWidget.setItem(int(cur_row), 5, QtWidgets.QTableWidgetItem("0"))
        cur = db.cursor()
        cur.execute(
            f"UPDATE orders SET status = 0 WHERE id = '{self.tableWidget.currentItem().text()}'"
        )
        db.commit()
        cur.close()

    def odobrit(self):
        cur_row = self.tableWidget.currentRow()
        self.tableWidget.setItem(int(cur_row), 5, QtWidgets.QTableWidgetItem("1"))
        cur = db.cursor()
        cur.execute(
            f"UPDATE orders SET status = 1 WHERE id = '{self.tableWidget.currentItem().text()}'"
        )
        db.commit()
        cur.close()

    def loaddata(self):
        cur = db.cursor()
        rows = cur.execute("SELECT * FROM orders")
        data = list(cur.fetchall())
        cur.close()
        row = 0
        self.tableWidget.setRowCount(len(data))
        for order in data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(order[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(order[1])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(order[2])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(order[3])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(order[4])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(order[5])))
            row += 1

    def go_to_login(self):
        self.log_in = Login_Window()
        self.log_in.show()
        self.close()


class Login_Window(QtWidgets.QMainWindow, Ui_Login_Window):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.open_reg)
        self.pushButton.clicked.connect(self.open_profile)

    def open_profile(self):
        curr = db.cursor()
        curr.execute(
            f"SELECT * FROM users WHERE login = '{self.lineEdit.text()}' and pass = '{self.lineEdit_2.text()}'"
        )
        exist = curr.fetchone()
        curr.close()

        if exist is not None:
            cur = db.cursor()
            cur.execute(
                f"SELECT id, login, pass FROM users WHERE login = '{self.lineEdit.text()}' and pass = '{self.lineEdit_2.text()}'"
            )
            res = list(cur.fetchone())
            info["id_user"] = res[0]
            info["login"] = res[1]
            info["password"] = res[2]
            if info["login"] == "admin" and info["password"] == "admin":
                self.admin_form = Admin_Form()
                self.admin_form.show()
                self.close()
            else:
                self.profilec = Profilek(login=info["login"], pwd=info["password"])
                self.profilec.show()
                self.close()

        else:
            self.error_message = QLabel(self)
            self.error_message.setText("Неверный логин или пароль")
            self.error_message.move(70, 160)
            self.error_message.adjustSize()
            self.error_message.show()

    def open_reg(self):
        try:
            self.reg_win = Reg_Win()
            self.reg_win.show()
            self.close()
        except Exception as e:
            err_mess = QLabel(self)
            err_mess.setText("Недопустимые значения")
            err_mess.move(100, 200)
            err_mess.adjustSize()
            err_mess.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Login_Window()
    w.show()
    sys.exit(app.exec())
