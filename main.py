from PyQt5.QtWidgets import QApplication
from View.GUI import TradingWindow
from Model.main_model import Model
from Control.updater import Updater
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    m = Model()
    window = TradingWindow(m)
    window.setWindowTitle('Trading monitor')
    u = Updater(m, window)

    app.exec_()
