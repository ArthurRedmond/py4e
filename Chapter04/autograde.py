def computepay(h, r):
    h = float(h)
    r = float(r)

    if(h > 10):
        regPay = 40 * r
        totalPay = regPay + ((h-40) * (r * 1.5))
    else:
        totalPay = h * r

    return totalPay

hrs = input("Enter Hours:")
rt = input("Enter Rate:")
p = computepay(hrs, rt)
print("Pay", p)