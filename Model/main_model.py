

from Model.moex_parse import parse_moex
from Model.DataBase.sqllite_db import sql_db


class Model:
    def __init__(self):
        self.parser = parse_moex()
        self.db = sql_db()

    def _get_tickers(self):
        tickers = self.db.get_all_tickets()
        return tickers

    def _parse_info(self):
        tickers = self._get_tickers()
        info = self.parser.get_current_info(tickers)
        return info

    def insert_info(self, ticker, price, target_price):
        self.db.insert_ticker(ticker, price, target_price)

    def delete_info(self, ticker):
        self.db.delete_ticker(ticker)

    def edit_info(self, ticker, price, target_price):
        self.db.edit_ticker(ticker, price, target_price)

    def update_info(self):
        self.db.update_db(self._parse_info())

    def get_info_from_db(self):
        return self.db.get_all_tickets()


if __name__ == '__main__':
    model = Model()
    model.update_info()
    model.get_info_from_db()