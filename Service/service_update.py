from typing import Iterable, Callable
from PyQt5.QtWidgets import QWidget
from Ui_service import Ui_Form_update_service
from database import Service, get_session


class ServiceUpdate(QWidget, Ui_Form_update_service):

    def __init__(self, service: Service, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_button_save1.clicked.connect(self.update_service)
        self.push_button_undo1.clicked.connect(lambda: self.close())


        self.label_id.setText(str(service.id))
        self.line_edit_doctor_id1.setText(str(service.doctor_id))
        self.line_edit_title1.setText(str(service.title))
        self.line_edit_price1.setText(str(service.price))

    def update_service(self):
        #data = {
         #   "doctor_id": self.line_edit_doctor_id1.text(),
          #  "title": self.line_edit_title1.text(),
         #   "price": self.line_edit_price1.text(),
         #   "service_id": int(self.label_id.text())
       # }
        #exist_service = self.session.query(Service).get(data["service_id"])
       # self.session.add(new_service)
       # self.session.commit()
       #self.custom_close()

        doctor_id = self.line_edit_doctor_id1.text()
        title = self.line_edit_title1.text()
        price = self.line_edit_price1.text()
        service_id = int(self.label_id.text())
        exist_service: Service = self.session.query(Service).get(service_id)
        exist_service.doctor_id = doctor_id
        exist_service.title = title
        exist_service.price = price
        self.session.commit()
        self.custom_close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()