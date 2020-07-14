import urllib.request
import xml.etree.ElementTree as ET
import ssl


class parse_moex:
    def __init__(self):
        pass
    # def check_db_boardid(self):
    #     pass

    def get_board_id(self, ticker):
        url = 'https://iss.moex.com./iss/securities.xml?q={}'.format(ticker)
        context = ssl._create_unverified_context()
        xml_file = urllib.request.urlopen(url, context=context)

        tree = ET.parse(xml_file)
        root = tree.getroot()

        for child in root[0][1]:
            if child.attrib['secid'] == ticker:
                board_id = child.attrib['primary_boardid']
        return board_id

    def get_current_info(self, tickers):
        url = 'https://iss.moex.com/iss/engines/stock/markets/shares/boards/' \
                'TQBR/securities.xml?iss.meta=off&iss.only=cecurities&securities.' \
                'columns=SECID,PREVADMITTEDQOUTE'

        xml_file = urllib.request.urlopen(url)

        tree = ET.parse(xml_file)
        root = tree.getroot()
        info_list = {}
        for ticker in tickers:
            for child in root[1]:
                for sub in child:
                    if sub.attrib['SECID'] == ticker:
                        current_price = float(sub.attrib['LAST'])
                        open_price = float(sub.attrib['OPEN'])
                        low_price = float(sub.attrib['LOW'])
                        high_price = float(sub.attrib['HIGH'])
                        info_list[ticker] = [current_price, [open_price, low_price, high_price]]

        # print('from parse:', info_list)
        return info_list

