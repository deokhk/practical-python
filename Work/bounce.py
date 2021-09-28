# bounce.py
#
# Exercise 1.5

num_bounce = 0
meter = 100

while num_bounce <10:
    num_bounce = num_bounce + 1
    meter = meter * 0.6
    print(num_bounce, round(meter, ndigits=4))