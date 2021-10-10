# 1.28.py
#
# Exercise 1.28

import gzip
with gzip.open("../Data/portfolio.csv.gz", "rt") as f:
    for line in f:
        print(line, end="")