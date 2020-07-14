
from PyQt5.QtWidgets import QGridLayout, QMainWindow, QWidget, QApplication, QPushButton

from View.plotting import PlotCanvas
from View.stokcs_table import stocks_table
from View.ticker_info import ticker_info
from Control.buttons import ButtonBox
import sys


class TradingWindow(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.initUI()

    def initUI(self):
        self.ticker_info = ticker_info()
        self.table = stocks_table(ticker_info=self.ticker_info)
        self.buttons = ButtonBox(self.table, self.model)
        self.pc = PlotCanvas(self, width=5, height=4)

        button = QPushButton("Отобразить график")
        button.setFixedSize(150, 25)
        grid = QGridLayout()
        grid.addLayout(self.buttons.get_box(), 0, 0, 1, 2)
        grid.addWidget(self.table.get_table(), 1, 0, 1, 2)
        grid.addLayout(self.ticker_info.get_info_grid(), 1, 3)
        grid.addWidget(button, 0, 4)
        grid.addWidget(self.pc, 1, 4)
        grid.setContentsMargins(10,10,10,10)
        grid.setSpacing(10)

        central_widget = QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)
        self.show()

    def fill_view(self, new_info):
        self.table.fill_table(new_info)

    def update_view(self, new_info):
        self.table.update_table(new_info)

    def get_table(self):
        return self.table

    # def plotDoubleClick(self):
    #     row = self.list.currentRow()
    #     item = self.list.item(row).text()
    #     print('row: ', row, ' item: ', item)
    #
    #     # self.pc.update_figure(candle_info(item))
    #     # self.box_current_text.setText(str(get_current_price(item)))
    #
    #     self.box_buy_text.setText(str(self.proList[item][0]))
    #     self.box_wish_text.setText(str(self.proList[item][1]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TradingWindow()

    # галимый подгон
    window.setFixedSize(1148, 450)
    window.setWindowTitle('Trading monitor')

    app.exec_()