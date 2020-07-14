
from PyQt5.QtWidgets import QGridLayout, QLabel

class ticker_info():
    def __init__(self):
        self.textgrid = QGridLayout()
        self.create_text()

    def create_text(self):

        box_open = QLabel("Open: ")
        box_open.setFixedSize(100, 15)
        box_low = QLabel("Low: ")
        box_low.setFixedSize(100, 15)
        box_high = QLabel("High: ")
        box_high.setFixedSize(100, 15)
        box_range = QLabel("Daily range: ")
        box_range.setFixedSize(100, 15)

        self.box_open_text = QLabel()
        self.box_open_text.setFixedSize(100, 15)
        self.box_low_text = QLabel()
        self.box_low_text.setFixedSize(100, 15)
        self.box_high_text = QLabel()
        self.box_high_text.setFixedSize(100, 15)
        self.box_range_text = QLabel()
        self.box_range_text.setFixedSize(100, 15)

        self.textgrid.addWidget(box_open, 0, 0)
        self.textgrid.addWidget(self.box_open_text, 0, 1)

        self.textgrid.addWidget(box_low, 1, 0)
        self.textgrid.addWidget(self.box_low_text, 1, 1)

        self.textgrid.addWidget(box_high, 2, 0)
        self.textgrid.addWidget(self.box_high_text, 2, 1)

        self.textgrid.addWidget(box_range, 3, 0)
        self.textgrid.addWidget(self.box_range_text, 3, 1)

        self.textgrid.setRowStretch(4, 1)

    def set_text_info(self, open_p=0, low=0, high=0):
        self.box_open_text.setText(str(open_p))
        self.box_low_text.setText(str(low))
        self.box_high_text.setText(str(high))
        self.box_range_text.setText(str(open_p) + ' - ' + str(high))

    def get_info_grid(self):
        return self.textgrid
