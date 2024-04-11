from typing import Iterable, Callable

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog

from database import get_session, Service
from Ui_service import Ui_Dialog_service


class Dialog_service(QDialog, Ui_Dialog_service):
    def __init__(self, text: str):
        super().__init__()
        self.setupUi(self)
        self.textBrowser.setText(text)