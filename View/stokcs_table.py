
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


class stocks_table():

    def __init__(self, ticker_info=[]):
        self.ticker_info = ticker_info
        self.table = QTableWidget()
        self.table.setMinimumSize(641, 400)
        self.format_table()
        self.table.cellClicked.connect(self.table_click)
        self.info = []

    def set_info(self, info):
        self.info = info

    def format_table(self):
        self.table.setColumnCount(6)  # Устанавливаем колонки

        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(["Ticker",
                                              "Покупка",
                                              "Текущая цена",
                                              "Целевая цена",
                                              "% от покупки",
                                              "% до цели"])

    def fill_table(self, data):
        # заполняем первую строку
        #TODO сделать переопределение метода после первого использования
        key = data.keys()
        for i in key:
            buy_price = data[i][0]
            target_price = data[i][1]
            # current_price = data[i][2]

            rowPosition = self.table.rowCount()
            self.table.insertRow(rowPosition)
            self.table.setItem(rowPosition, 0, QTableWidgetItem(i))
            self.table.setItem(rowPosition, 1, QTableWidgetItem(str(buy_price)))
            # self.table.setItem(rowPosition, 2, QTableWidgetItem(str(current_price)))
            self.table.setItem(rowPosition, 3, QTableWidgetItem(str(target_price)))
            self.table.setSortingEnabled(True)
            self.sort_changer = 1
            # rowPosition = self.rowCount()
            # self.insertRow(rowPosition)
            # self.setItem(rowPosition, 0, QTableWidgetItem(i))
            # self.setItem(rowPosition, 1, QTableWidgetItem(str(buy_price)))
            # self.setItem(rowPosition, 3, QTableWidgetItem(str(target_price)))

    def update_table(self, data):
        row = 0
        for i in data.keys():
            buy_price = data[i][0]
            target_price = data[i][1]
            current_price = data[i][2]
            percent_buy = round((current_price * 100 / buy_price) - 100, 2)
            percent_target = round((current_price * 100 / target_price) - 100, 2)

            item_buy = QTableWidgetItem(str(percent_buy))
            item_target = QTableWidgetItem(str(percent_target))

            if percent_buy < 0:
                item_buy.setBackground(QColor('red'))
            else:
                item_buy.setBackground(QColor('green'))

            if percent_target > -5:
                item_target.setBackground(QColor('red'))


            self.table.setItem(row, 2, QTableWidgetItem(str(current_price)))
            self.table.setItem(row, 4, item_buy)
            self.table.setItem(row, 5, item_target)
            row += 1

    def add_in_table(self, item, buy_price, target_price):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        self.table.setItem(rowPosition, 0, QTableWidgetItem(item))
        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(buy_price)))
        self.table.setItem(rowPosition, 3, QTableWidgetItem(str(target_price)))

    def edit_t(self, buy_price, target_price):
        rowPosition = self.table.currentRow()
        print(rowPosition)
        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(buy_price)))
        self.table.setItem(rowPosition, 3, QTableWidgetItem(str(target_price)))

    def sort(self):
        col = self.table.currentColumn()
        if self.sort_changer == 1:
            self.table.sortByColumn(col, Qt.SortOrder(1))
            self.sort_changer = 0
        else:
            self.table.sortByColumn(col, Qt.SortOrder(0))
            self.sort_changer = 1

    def remove(self, row):
        self.table.removeRow(row)

    def get_current_row_ticker(self):
        row = self.table.currentRow()
        ticker = self.table.item(row, 0).text()
        return row, ticker

    def get_table(self):
        return self.table

    def table_click(self, row, col):
        item = self.table.item(row, 0).text()
        o = self.info[item]
        self.ticker_info.set_text_info(o[3], o[4], o[5])
