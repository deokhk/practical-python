# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_period = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    total_period +=1
    if total_period >= extra_payment_start_month and total_period <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        if principal < 0:
            total_paid = total_paid + payment + extra_payment + principal
            principal = 0
        else:
            total_paid +=( payment + extra_payment)

    else:
        principal = principal * (1+rate/12) - payment
        if principal < 0:
            total_paid = total_paid + payment + principal
            principal = 0
        else:
            total_paid += payment

    print(f"{total_period} {round(total_paid,ndigits=2)} {round(principal,ndigits=2)}")

print(f"Total paid {round(total_paid,ndigits=1)}")
print(f"Months {total_period}")