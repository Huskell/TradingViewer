from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QGridLayout, QLabel, QCompleter
from Model.DataBase.tickers_list import comp_list

class addDialog(QDialog):
    def __init__(self, table, model, parent=None):
        super(addDialog, self).__init__(parent)
        self.table = table
        self.model = model

        add_grid = QGridLayout()
        add_grid.addWidget(QLabel('Введите тикер'), 0, 0)
        add_grid.addWidget(QLabel('Цена покупки'), 1, 0)
        add_grid.addWidget(QLabel('Целевая цена'), 2, 0)

        self.ticker = QLineEdit()
        completer = QCompleter(comp_list, self.ticker)
        self.ticker.setCompleter(completer)

        self.buy_price = QLineEdit()
        self.target_price = QLineEdit()
        add_grid.addWidget(self.ticker, 0, 1)
        add_grid.addWidget(self.buy_price, 1, 1)
        add_grid.addWidget(self.target_price, 2, 1)

        button_ok = QPushButton("Добавить")
        button_ok.clicked.connect(self.add)

        button_cancel = QPushButton("Отмена")
        button_cancel.clicked.connect(self.closing)

        add_grid.addWidget(button_ok, 3, 0)
        add_grid.addWidget(button_cancel, 3, 1)

        self.setLayout(add_grid)

    def add(self):
        self.model.insert_info(self.ticker.text(), float(self.buy_price.text()), float(self.target_price.text()))
        self.table.add_in_table(self.ticker.text(), float(self.buy_price.text()), float(self.target_price.text()))
        return self.close()

    def closing(self):
        return self.close()
