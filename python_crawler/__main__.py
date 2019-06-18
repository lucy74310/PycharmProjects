import ssl
import sys
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen

import pandas as pd
from bs4 import BeautifulSoup


def crawling_pelicana():
    results = []

    # count(시작점) 무한대로감, break 반드시 필요
    for page in count(start=113):
        url = 'https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % page
        try:
            request = Request(url)
            # ssl._create_default_https_context = ssl._create_unverified_context()
            context = ssl._create_unverified_context()
            response = urlopen(request, context=context)

            receive = response.read()
            html = receive.decode('utf-8', errors='replace')

            print(f'{datetime.now()}: success for request [{url}]')
        except Exception as e:
            # datetime 밑에꺼 import
            print(f'{e} : {datetime.now()}', file=sys.stderr)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            # tag 다 빼고 string 만
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]
            t = (name, address) + tuple(sidogu)
            results.append(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gu'])
    table.to_csv('__results__/pelicana.csv', encoding='utf-8', mode='w', index=True)

    # for t in results:
    #     print(t)


def crawling_nene():
    results = []

    before_page_first_shop = ''

    for page in count(start=1):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?ex_select=1&ex_select2=&IndexSword=&GUBUN=A&page=%d' % page

        try:
            request = Request(url)
            response = urlopen(request)
            receive = response.read()
            html = receive.decode('utf-8')

            print(f'{datetime.now()} : success for request[{url}]')
        except Exception as e:
            print(f'{datetime.now()} : {e}', file=sys.stderr)
            break

        bs = BeautifulSoup(html, 'html.parser')

        wrap_div = bs.find('div', attrs={'class': 'shopWrap'})

        shop_divs = wrap_div.findAll('div', attrs={'class': 'shopInfo'})

        now_page_first_shop = wrap_div.find('div', attrs={'class': 'shopName'}).text

        # 끝 검출
        if now_page_first_shop == before_page_first_shop:
            break

        for index, shop in enumerate(shop_divs):
            strings = list(shop.strings)

            if strings[2] != 'Pizza':
                name = strings[4]
                address = strings[6]
            else:
                name = strings[6]
                address = strings[8]

            dosigu = address.split()[:2]
            t = (name, address) + tuple(dosigu)

            if index == 0:
                before_page_first_shop = name

            results.append(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gu'])
    table.to_csv('__results__/nene.csv', encoding='utf-8', mode='w', index=True)


if __name__ == '__main__':
    # pelicana

    # 처음에 에러 SSL: CERTIFICATE_VERIFY_FAILED
    # SSL 무시하도록 crawling_pelicana()에 아래 두줄 추가
    # context=ssl._create_unverified_context()
    # response=urlopen(request, context=context)

    # crawling_pelicana()

    #nene 과제
    crawling_nene()
