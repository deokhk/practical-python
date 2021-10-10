"""
Practice 1.28/1.30/1.31/1.32/1.33

"""
import csv
import sys
def portfolio_cost(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        total_cost = 0
        for row in rows:
            try:
                num_shares = int(row[1])
                price = float(row[2])
                total_cost += num_shares * price
            except ValueError:
               print("Couldn't parse", row)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
    
cost = portfolio_cost("Data/missing.csv")
print("Total cost:", cost)
