import sqlite3 as sql


class sql_db:
    def __init__(self):
        self.path = "Model/DataBase/mydatabase.db"
        # self.path = "mydatabase.db"

    def insert_ticker(self, ticker, price, target_price):
        db = sql.connect(self.path)
        entities = (ticker, price, target_price)
        cursor = db.cursor()
        cursor.execute('''INSERT INTO stocks(ticker, buy_price, target_price) VALUES(?, ?, ?)''', entities)
        db.commit()
        db.close()

    def delete_ticker(self, ticker):
        db = sql.connect(self.path)
        cursor = db.cursor()
        cursor.execute('''DELETE FROM stocks WHERE ticker=:t''', {'t': ticker})
        db.commit()
        db.close()

    def edit_ticker(self, ticker, buy_price, target_price):
        db = sql.connect(self.path)
        cursor = db.cursor()
        cursor.execute('''UPDATE stocks 
                            SET buy_price=:b_p, target_price=:t_p
                            WHERE ticker=:t''', {'t': ticker,
                                                 'b_p': buy_price,
                                                 't_p': target_price})
        db.commit()
        db.close()
        
    def get_all_tickets(self):
        db = sql.connect(self.path)
        cursor = db.cursor()
        cursor.execute('''SELECT ticker, 
                            buy_price, 
                            target_price,
                            current_price,
                            open_price,
                            low_price,
                            high_price 
                            FROM stocks''')
        tickers_list = cursor.fetchall()
        db.close()
        tick_price = {}
        for i in tickers_list:
            tick_price[i[0]] = [i[1], i[2], i[3], i[4], i[5], i[6]]

        # print('from db:', tick_price)
        return tick_price

    def update_db(self, info):
        db = sql.connect(self.path)
        for i in info.keys():
            current_price, open_price, low_price, high_price = info[i][0], info[i][1][0], info[i][1][1], info[i][1][2]
            cursor = db.cursor()
            cursor.execute('''UPDATE stocks
                                SET current_price=:c_p, 
                                    open_price=:o_p, 
                                    low_price=:l_p, 
                                    high_price=:h_p
                                WHERE ticker=:t''', {"t":i,
                                                     "c_p": current_price,
                                                     "o_p": open_price,
                                                     "l_p": low_price,
                                                     "h_p": high_price
                                                     })
            db.commit()
        db.close()
