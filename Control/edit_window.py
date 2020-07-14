from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QGridLayout, QLabel


class editDialog(QDialog):
    def __init__(self, table, model, parent=None):
        super(editDialog, self).__init__(parent)
        self.table = table
        self.model = model
        self.row, self.ticker = self.table.get_current_row_ticker()
        add_grid = QGridLayout()
        add_grid.addWidget(QLabel('Текущий тикер'), 0, 0)
        add_grid.addWidget(QLabel('Цена покупки'), 1, 0)
        add_grid.addWidget(QLabel('Целевая цена'), 2, 0)

        self.tick = QLabel()
        self.tick.setText(self.ticker)
        self.buy_price = QLineEdit()
        self.buy_price.setText('Новая цена')
        self.target_price = QLineEdit()
        self.target_price.setText('Новая цена')
        add_grid.addWidget(self.tick, 0, 1)
        add_grid.addWidget(self.buy_price, 1, 1)
        add_grid.addWidget(self.target_price, 2, 1)

        button_ok = QPushButton("Редактировать")
        button_ok.clicked.connect(self.edit)

        button_cancel = QPushButton("Отмена")
        button_cancel.clicked.connect(self.closing)

        add_grid.addWidget(button_ok, 3, 0)
        add_grid.addWidget(button_cancel, 3, 1)

        self.setLayout(add_grid)

    def edit(self):
        self.table.edit_t(float(self.buy_price.text()), float(self.target_price.text()))
        self.model.edit_info(self.ticker, float(self.buy_price.text()), float(self.target_price.text()))
        return self.close()

    def closing(self):
        return self.close()