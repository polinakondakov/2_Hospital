from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog

from Doctor.Ui_doctor import Ui_MainWindow_doctor
from Doctor.doctor_create import DoctorCreate
from Doctor.doctor_update import DoctorUpdate
from Service.dialog_service import Dialog_service
from database import get_session, Doctor


class DoctorTable(QMainWindow, Ui_MainWindow_doctor):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_window = None
        self.session = get_session()
        self.current_row = None
        self.push_button_doctor_create.clicked.connect(self.open_doctor_create)
        self.tableWidget.cellDoubleClicked.connect(self.open_doctor_update)
        self.push_button_doctor_delete.clicked.connect(self.open_dialog_delete_doctor)
        self.tableWidget.cellClicked.connect(self.table_widget_cell_clicked)

        self.update_table()

    def update_table(self):
        doctors = self.session.query(Doctor).order_by(Doctor.id).all()
        self.tableWidget.setRowCount(0)
        for doctor in doctors:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(doctor.id)))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(doctor.full_name))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(doctor.specialisation))

    def table_widget_cell_clicked(self, row, column):
        self.current_row = row


    def open_doctor_create(self):
        self.create_window = DoctorCreate([self.update_table])
        self.create_window.show()

    def open_doctor_update(self, row, column):
        doctor_id = int(self.tableWidget.item(row, 0).text())
        doctor = self.session.query(Doctor).get(doctor_id)
        self.create_window = DoctorUpdate(doctor, [self.update_table])
        self.create_window.show()

    def open_dialog_delete_doctor(self):
        if self.current_row is None:
            return
        dialog_delete = Dialog_service("Точно хотите удалить??")
        ret_value = dialog_delete.exec_()
        if ret_value == QDialog.Accepted:
            doctor_id = int(self.tableWidget.item(self.current_row, 0).text())
            doctor = self.session.query(Doctor).get(doctor_id)
            self.session.delete(doctor)
            self.session.commit()
            self.update_table()




