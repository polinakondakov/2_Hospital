import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

from Doctor.doctor_table import DoctorTable
from Service.service_table import ServiceTable
from Ui import Ui_Form_no_password
from Ui.ui_main_menu import Ui_Form_main_menu
from Ui.ui_menu import Ui_Form_menu
from Ui.ui_password import Ui_Form_password
from Ui.ui_usi_pochki import Ui_Form_pochki
from ui_user_exit import Ui_Form_user_exit
from ui_user_regestrion import Ui_Form_user_regestration

# ошибки
sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook

#Главное меню
class Main_menu(QWidget, Ui_Form_main_menu):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.push_button_like_admin.clicked.connect(self.open_password)
        self.push_button_like_patient.clicked.connect(self.open_users)

    def open_password(self):
        self.window = Password()
        self.window.show()

    def open_users(self):
        self.window = Users()
        self.window.show()

#Окошко ввода пароля
class Password(QWidget, Ui_Form_password):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chek) #можно заходить и по кнопке
    def chek(self):
        if self.lineEdit.text() == "198687":
            self.window = Menu()
            self.window.show()
        else:
            self.window = No_Password()
            self.window.show()
            self.close()
        self.close()
    def keyPressEvent(self, event): #можно заходить жмякнув enter
        if event.key() == Qt.Key_Return:
            self.chek()

#Сообщение об ошибке
class No_Password(QWidget, Ui_Form_no_password):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)

#Меню выбора
class Menu(QWidget, Ui_Form_menu):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.push_button_service.clicked.connect(self.open_service)
        self.push_button_appointment.clicked.connect(self.open_appointment)
        self.pushButton_doctor.clicked.connect(self.open_doctor)

    def open_service(self):
        self.window = ServiceTable()
        self.window.show()
    def open_appointment(self):
        self.window = Usi_pochki()
        self.window.show()
    def open_doctor(self):
        self.window1 = DoctorTable()
        self.window1.show()

class Usi_pochki(QWidget, Ui_Form_pochki):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)

class Users(QWidget, Ui_Form_user_exit):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.push_button_registration_reg_3.clicked.connect(self.open_registration_users)

    def open_registration_users(self):
        self.window = Registration_users()
        self.window.show()

class Registration_users(QWidget, Ui_Form_user_regestration):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        #когда юзер нажмет зарегистрироваться вызовется функция создания пациента

app = QApplication(sys.argv)
ex_Main_menu = Main_menu()
ex_Main_menu.show()
sys.exit(app.exec_())
