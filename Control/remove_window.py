from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QGridLayout, QLabel, QCompleter
from Model.DataBase.tickers_list import comp_list

class removeDialog(QDialog):
    def __init__(self, table, model, parent=None):
        super(removeDialog, self).__init__(parent)
        self.table = table
        self.model = model
        self.row, self.ticker = self.table.get_current_row_ticker()

        add_grid = QGridLayout()
        add_grid.addWidget(QLabel('Вы уверены что хотите удалить - ' + str(self.ticker)), 0, 0, 1, 2)

        button_ok = QPushButton("Удалить")
        button_ok.clicked.connect(self.remove)

        button_cancel = QPushButton("Отмена")
        button_cancel.clicked.connect(self.closing)

        add_grid.addWidget(button_ok, 1, 0)
        add_grid.addWidget(button_cancel, 1, 1)

        self.setLayout(add_grid)

    def remove(self):
        self.table.remove(self.row)
        self.model.delete_info(self.ticker)
        return self.close()

    def closing(self):
        return self.close()