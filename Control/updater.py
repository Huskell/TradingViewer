from PyQt5.QtCore import QTimer


class Updater:
    def __init__(self, model, view):
        self.model = model
        self.info = self.model.get_info_from_db()
        self.view = view
        self.view.fill_view(self.info)
        self.table = self.view.get_table()
        self.table.set_info(self.info)

        self.timeout_action()
        self.start_timer()

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout_action)
        self.timer.start(30000)

    def timeout_action(self):
        self.model.update_info()
        self.info = self.model.get_info_from_db()
        self.table.set_info(self.info)

        print('in timer info:', self.info)
        self.view.update_view(self.info)

