"""
Practice 1.30

"""
def portfolio_cost(filename):
    with open(filename) as f:
        headers = next(f)
        total_cost = 0
        for line in f:
            line = line.split(",")
            num_shares = int(line[1])
            price = float(line[2])
            total_cost += num_shares * price
    return total_cost

cost = portfolio_cost("../Data/missing.csv")
print("Total cost:", cost)
