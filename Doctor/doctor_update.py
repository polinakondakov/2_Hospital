from typing import Iterable, Callable
from PyQt5.QtWidgets import QWidget
from Doctor.Ui_doctor.ui_doctor_update import Ui_Form_doctor_update
from database import get_session, Doctor


class DoctorUpdate(QWidget, Ui_Form_doctor_update):

    def __init__(self, doctor: Doctor, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_button_save1.clicked.connect(self.update_doctor)
        self.push_button_undo1.clicked.connect(lambda: self.close())


        self.label_id.setText(str(doctor.id))
        self.line_edit_doctor_fio1.setText(str(doctor.full_name))
        self.line_edit_specialisation1.setText(str(doctor.specialisation))

    def update_doctor(self):
        full_name = self.line_edit_doctor_fio1.text()
        specialisation = self.line_edit_specialisation1.text()
        doctor_id = int(self.label_id.text())
        exist_doctor: Doctor = self.session.query(Doctor).get(doctor_id)
        exist_doctor.full_name = full_name
        exist_doctor.specialisation = specialisation
        self.session.commit()
        self.custom_close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()