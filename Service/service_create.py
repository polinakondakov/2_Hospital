from typing import Iterable, Callable
from PyQt5.QtWidgets import QWidget
from Ui_service import Ui_Form_service
from database import Service, get_session

class ServiceCreate(QWidget, Ui_Form_service):

    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_button_save.clicked.connect(self.create_service)
        self.push_button_undo.clicked.connect(lambda: self.close())

    def create_service(self):
        doctor_id = self.line_edit_doctor_id.text()
        title = self.line_edit_title.text()
        price = self.line_edit_price.text()
        new_service = Service(doctor_id=doctor_id,
                              title=title,
                              price=price)
        self.session.add(new_service)
        self.session.commit()

        self.custom_close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()