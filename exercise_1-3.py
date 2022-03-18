from http.client import PAYMENT_REQUIRED


hours = input("Enter hours: ")
rate = input("Enter rate: ")
pay = float(hours) * float(rate)
print("Pay:", str(pay))
