from PyQt5.QtWidgets import QPushButton, \
    QHBoxLayout

from Control.add_window import addDialog
from Control.remove_window  import removeDialog
from Control.edit_window import editDialog
import sys


class ButtonBox:
    def __init__(self, table, model):
        self.table = table
        self.model = model
        self.buttonBox = QHBoxLayout()
        self.create_box()

    def create_box(self):
        for text, slot in (("Add", self.add),
                           ("Edit", self.edit),
                           ("Remove", self.remove),
                           ("Sort", self.table.sort),
                           ("Close", self.close)):
            button = QPushButton(text)

            self.buttonBox.addWidget(button)
            button.clicked.connect(slot)

    def get_box(self):
        return self.buttonBox

    def add(self):
        aw = addDialog(self.table, self.model)
        aw.exec_()

    def edit(self):
        aw = editDialog(self.table, self.model)
        aw.exec_()

    def remove(self):
        aw = removeDialog(self.table, self.model)
        aw.exec_()

    @staticmethod
    def close():
        sys.exit()

