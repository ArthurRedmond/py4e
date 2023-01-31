hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
errorMessage = "Error, please enter numeric input"

def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)

        if(hours > 40):
            pay = (rate * 40.0) + ((hours - 40) * (rate * 1.5))
        else:
            pay = hours * rate

        print("Pay: " + str(pay))

    except:
       print(errorMessage)

computepay(hours, rate)