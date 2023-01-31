hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

h = float(hrs)
rate = float(rate)

if(h > 40):
    pay = (rate * 40.0) + ((h - 40) * (rate * 1.5))
else:
    pay = h * rate

print("Pay: " + str(pay))