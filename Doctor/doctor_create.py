from typing import Iterable, Callable
from PyQt5.QtWidgets import QWidget
from Doctor.Ui_doctor.ui_doctor_create import Ui_Form_doctor_create
from database import get_session, Doctor


class DoctorCreate(QWidget, Ui_Form_doctor_create):

    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_button_save.clicked.connect(self.create_doctor)
        self.push_button_undo.clicked.connect(lambda: self.close())

    def create_doctor(self):
        full_name = self.line_edit_full_name_doctor.text()
        specialisation = self.line_edit_specialisation.text()
        new_service = Doctor(full_name = full_name,
                              specialisation = specialisation,)
        self.session.add(new_service)
        self.session.commit()

        self.custom_close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()