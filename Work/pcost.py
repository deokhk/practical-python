"""
Practice 1.28/1.30/1.31/1.32/1.33

"""
import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total_cost = 0
    for stock in portfolio:
        total_cost += stock.shares* stock.price
    return total_cost

def main(argv):
    portfile = argv[1]
    total_cost = portfolio_cost(portfile)
    print(f'Total cost: {total_cost}')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]}' 'portfile')
    main(sys.argv)