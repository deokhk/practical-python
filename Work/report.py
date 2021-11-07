# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {}
            holding["name"] = row[0]
            holding["shares"] = int(row[1])
            holding["price"] = float(row[2])
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print("Empty row on the file:", row)
    return prices

def check_portfolio_and_gain():
    portfolio = read_portfolio("Data/portfolio.csv")
    prices = read_prices("Data/prices.csv")    

    Total_gain = 0
    Total_value = 0
    for holding in portfolio:
        name = holding["name"]
        buying_price = holding["price"]
        buying_quantity = holding["shares"]
        current_price = prices[name]
        Total_value += current_price * buying_quantity
        Total_gain += (current_price - buying_price) * buying_quantity

    print("Total value of portfolio: ", Total_value)
    print("Total gain of portfolio: ", Total_gain)

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        name = holding["name"]
        buying_price = holding["price"]
        shares = holding["shares"]
        current_price = prices[name]
        change = buying_price - current_price
        report.append((name, shares, current_price, change))
    return report


