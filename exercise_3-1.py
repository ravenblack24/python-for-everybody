hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = 0

if float(hours) > 40 :
  overtime = float(hours) - 40
  newRate = float(rate) * 0.5
  pay += overtime * newRate
pay += float(hours) * float(rate)

print("Pay:", pay)
