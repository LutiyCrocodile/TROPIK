# Form implementation generated from reading ui file 'C:\Users\Maks\PycharmProjects\PythonProject4\cabinetui.ui'
#
# Created by: PyQt6 UI code generator 6.9.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Cabi_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        Form.setMinimumSize(QtCore.QSize(500, 400))
        Form.setMaximumSize(QtCore.QSize(500, 400))
        self.cab = None
        self.tech = None
        self.cabinetlistWidget = QtWidgets.QListWidget(parent=Form)
        self.cabinetlistWidget.setGeometry(QtCore.QRect(-2, 40, 256, 192))
        self.cabinetlistWidget.setStyleSheet('font: 75 16pt "Rubik";')
        self.cabinetlistWidget.setObjectName("cabinetlistWidget")
        self.cabinetlistWidget.itemClicked.connect(self.on_cabinet_selected)
        self.listWidget_2 = QtWidgets.QListWidget(parent=Form)
        self.listWidget_2.setGeometry(QtCore.QRect(253, 40, 256, 192))
        self.listWidget_2.setStyleSheet('font: 75 16pt "Rubik";')
        self.listWidget_2.setObjectName("listWidget_2")

        self.listWidget_2.itemClicked.connect(self.on_technik_selected)

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet('font: 75 10pt "Rubik";')
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('font: 75 10pt "Rubik";')
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet('font: 75 10pt "Rubik";')
        self.label_3.setObjectName("label_3")
        self.datalineEdit = QtWidgets.QLineEdit(parent=Form)
        self.datalineEdit.setGeometry(QtCore.QRect(10, 280, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.datalineEdit.setFont(font)
        self.datalineEdit.setStyleSheet(
            'font: 75 10pt "Rubik";\n' "border: 1px solid #000;\n" "border-radius: 2px"
        )
        self.datalineEdit.setReadOnly(True)
        self.datalineEdit.setObjectName("datalineEdit")
        self.paralineEdit = QtWidgets.QLineEdit(parent=Form)
        self.paralineEdit.setGeometry(QtCore.QRect(90, 280, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.paralineEdit.setFont(font)
        self.paralineEdit.setStyleSheet(
            'font: 75 10pt "Rubik";\n' "border: 1px solid #000;\n" "border-radius: 2px"
        )
        self.paralineEdit.setReadOnly(True)
        self.paralineEdit.setObjectName("paralineEdit")
        self.cabinetlineEdit = QtWidgets.QLineEdit(parent=Form)
        self.cabinetlineEdit.setGeometry(QtCore.QRect(130, 280, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.cabinetlineEdit.setFont(font)
        self.cabinetlineEdit.setStyleSheet(
            'font: 75 10pt "Rubik";\n' "border: 1px solid #000;\n" "border-radius: 2px"
        )
        self.cabinetlineEdit.setReadOnly(True)
        self.cabinetlineEdit.setObjectName("cabinetlineEdit")
        self.techniklineEdit = QtWidgets.QLineEdit(parent=Form)
        self.techniklineEdit.setGeometry(QtCore.QRect(210, 280, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.techniklineEdit.setFont(font)
        self.techniklineEdit.setStyleSheet(
            'font: 75 10pt "Rubik";\n' "border: 1px solid #000;\n" "border-radius: 2px"
        )
        self.techniklineEdit.setReadOnly(True)
        self.techniklineEdit.setObjectName("techniklineEdit")
        self.send_pushButton = QtWidgets.QPushButton(parent=Form)
        self.send_pushButton.setGeometry(QtCore.QRect(310, 352, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(-1)
        self.send_pushButton.setFont(font)
        self.send_pushButton.setStyleSheet(
            "background-color: #b06e68;\n"
            "color: white;\n"
            "font-size: 18px;\n"
            "font-family: Rubik;\n"
            "border-radius: 1px;\n"
            "border: 2px solid #3f3f3f"
        )
        self.send_pushButton.setObjectName("pushButton")
        self.back_btn = QtWidgets.QPushButton(parent=Form)
        self.back_btn.setGeometry(QtCore.QRect(10, 352, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(-1)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(
            "background-color: #ebbdb9;\n"
            "color: black;\n"
            "font-size: 20px;\n"
            "font-family: Rubik;\n"
            "border-radius: 1px;\n"
            "border: 2px solid #3f3f3f"
        )
        self.back_btn.setObjectName("pushButton_2")
        self.cls_btn = QtWidgets.QPushButton(parent=Form)
        self.cls_btn.setGeometry(QtCore.QRect(90, 352, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(-1)
        self.cls_btn.setFont(font)
        self.cls_btn.setStyleSheet(
            "background-color: #ebbdb9;\n"
            "color: black;\n"
            "font-size: 20px;\n"
            "font-family: Rubik;\n"
            "border-radius: 1px;\n"
            "border: 2px solid #3f3f3f"
        )
        self.cls_btn.setObjectName("pushButton_4")

        self.cls_btn.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TROPIK — система бронирования"))
        self.label.setText(_translate("Form", "Выберите свободный кабинет:"))
        self.label_2.setText(_translate("Form", "Выберите свободную технику:"))
        self.label_3.setText(
            _translate(
                "Form", "<html><head/><body><p>Подтвердите ваш выбор:</p></body></html>"
            )
        )
        self.datalineEdit.setText(_translate("Form", "Дата"))
        self.paralineEdit.setText(_translate("Form", "Пара"))
        self.cabinetlineEdit.setText(_translate("Form", "Кабинет"))
        self.techniklineEdit.setText(_translate("Form", "Техника"))
        self.send_pushButton.setText(_translate("Form", "Отправить заявку"))
        self.back_btn.setText(_translate("Form", "Назад"))
        self.cls_btn.setText(_translate("Form", "Выход"))

    # Новые методы для обработки выбора
    def on_cabinet_selected(self, item):
        """Обновляет поле 'Кабинет' при выборе из списка."""
        self.cab = item
        self.cabinetlineEdit.setText(item.text())
        self.cab_id = item.data(QtCore.Qt.ItemDataRole.UserRole)  # Получаем ID
        self.cab_number = item.text()  # Получаем номер кабинета
        print(f"Выбран кабинет ID: {self.cab_id}, Номер: {self.cab_number}")
        # info["num_cab"] = cab_id  # Сохраняем ID в словарь

    def on_technik_selected(self, item):
        """Обновляет поле 'Техника' при выборе из списка."""
        self.tech = item
        self.techniklineEdit.setText(item.text())
        self.res_id = item.data(QtCore.Qt.ItemDataRole.UserRole)  # Получаем ID
        self.res_name = item.text()  # Получаем название
        print(f"Выбрана техника ID: {self.res_id}, Название: {self.res_name}")
        # info["technik"] = res_id  # Сохраняем ID в словарь


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Cabi_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
