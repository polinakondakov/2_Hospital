from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog

from Service.dialog_service import Dialog_service
from Service.service_create import ServiceCreate
from Service.service_update import ServiceUpdate
from Ui_service import Ui_MainWindow_service
from database import get_session, Service


class ServiceTable(QMainWindow, Ui_MainWindow_service):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_window = None
        self.session = get_session()
        self.current_row = None
        self.push_button_service_create.clicked.connect(self.open_service_create)
        self.tableWidget.cellDoubleClicked.connect(self.open_service_update)
        self.push_button_service_delete.clicked.connect(self.open_dialog_delete_service)
        self.tableWidget.cellClicked.connect(self.table_widget_cell_clicked)

        self.update_table()

    def update_table(self):
        services = self.session.query(Service).order_by(Service.id).all()
        self.tableWidget.setRowCount(0)
        for service in services:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(service.id)))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(service.doctor_id)))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(service.title))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(service.price)))

    def table_widget_cell_clicked(self, row, column):
        self.current_row = row


    def open_service_create(self):
        self.create_window = ServiceCreate([self.update_table])
        self.create_window.show()

    def open_service_update(self, row, column):
        service_id = int(self.tableWidget.item(row, 0).text())
        service = self.session.query(Service).get(service_id)
        self.create_window = ServiceUpdate(service, [self.update_table])
        self.create_window.show()

    def open_dialog_delete_service(self):
        if self.current_row is None:
            return
        dialog_delete = Dialog_service("Точно хотите удалить??")
        ret_value = dialog_delete.exec_()
        if ret_value == QDialog.Accepted:
            service_id = int(self.tableWidget.item(self.current_row, 0).text())
            service = self.session.query(Service).get(service_id)
            self.session.delete(service)
            self.session.commit()
            self.update_table()

#СДЕЛАТЬ ЧТОБ МОЖНО БЫЛО УДАЛЯТЬ НЕСКОЛЬКО СРАЗУ


