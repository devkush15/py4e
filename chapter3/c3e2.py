try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    pay = (hours - 40)*rate*1.5 + 40*rate
else:
    pay = hours*rate

print("Pay: ", pay)