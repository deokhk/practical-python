"""
Practice 1.28/1.30/1.31/1.32/1.33

"""
import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum([s.cost for s in portfolio])

def main(argv):
    portfile = argv[1]
    total_cost = portfolio_cost(portfile)
    print(f'Total cost: {total_cost}')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]}' 'portfile')
    main(sys.argv)