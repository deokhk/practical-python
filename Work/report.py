# report.py
#
# Exercise 2.4

import csv
import stock
from fileparse import parse_csv

def read_portfolio(filename: str) -> list:
    '''
    주식 포트폴리오 파일을 읽어 stock instance의 리스트를 생성.
    name, shares, price를 attribute로 가짐.
    '''
    with open(filename) as file:
        portdicts = parse_csv(file, select=['name', 'shares', 'price'], types=[str,int,float])
    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio

def read_prices(filename: str) -> dict:
    '''
    CSV 파일에서 이름과 가격 데이터를 읽음
    '''
    with open(filename) as file:
        pricelist = parse_csv(file, types=[str,float], has_headers=False)
    prices = dict(pricelist)
    return prices

def check_portfolio_and_gain():
    portfolio = read_portfolio("Data/portfolio.csv")
    prices = read_prices("Data/prices.csv")    

    Total_gain = 0
    Total_value = 0
    for holding in portfolio:
        name = holding.name
        buying_price = holding.price
        buying_quantity = holding.shares
        current_price = prices[name]
        Total_value += current_price * buying_quantity
        Total_gain += (current_price - buying_price) * buying_quantity

    print("Total value of portfolio: ", Total_value)
    print("Total gain of portfolio: ", Total_gain)

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        name = holding.name
        buying_price = holding.price
        shares = holding.shares
        current_price = prices[name]
        change = buying_price - current_price
        report.append((name, shares, current_price, change))
    return report

def print_report(report:dict):
    '''
    보고서를 출력
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_filename:str, prices_filename:str):
    '''
    report를 생성하고, report를 출력
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    main(sys.argv)

