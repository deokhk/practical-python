# report.py
#
# Exercise 2.4

import csv
import stock
import tableformat
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
        change = current_price - buying_price
        report.append((name, shares, current_price, change))
    return report

def print_report(reportdata:dict, formatter:tableformat.TableFormatter):
    '''
    보고서를 출력
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename:str, prices_filename:str, fmt:str='txt'):
    '''
    report를 생성하고, report를 출력
    '''
    # 데이터 파일 읽기
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # 보고서 데이터 생성
    report = make_report(portfolio, prices)
    
    # 프린트
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    portfile = argv[1]
    pricefile = argv[2]
    fmt = argv[3]
    portfolio_report(portfile, pricefile, fmt)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile fmt')
    main(sys.argv)

