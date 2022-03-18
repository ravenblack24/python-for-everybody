hours = input("Enter Hours: ")

try:
  floatHours = float(hours)
except:
  print("Error, please enter numeric input")
  quit()

try:
  rate = input("Enter Rate: ")
  floatRate = float(rate)
except:
  print("Error, please enter numeric input")
  quit()

pay = 0

if floatHours > 40 :
  overtime = floatHours - 40
  newRate = floatRate * 0.5
  pay += overtime * newRate
pay += floatHours * floatRate

print("Pay:", pay)
