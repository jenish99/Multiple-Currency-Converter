from forex_python.converter import CurrencyRates
import sys
import keyboard
from num2words import num2words

print("Welcome To Currency Converter.!!")
print("================================")

value = input("Enter Amount: ")
#print(value)
FC = input("From Currency: ")
#print(FC)
c = CurrencyRates()
d = c.get_rates(FC)
TC = input("To Currency: ")
#print(TC)


result = float(value)*d[TC]
print('Final Result:',round(result,2))
print(num2words(round(result,2)))
#print("=====BY: JENISH SHIVSHAKTIWALA======")
print("================================")
print("Other Conversions")
#print(d)
for rates in d:
    if rates=="USD" or rates=="EUR" or rates=="THB" or rates=="IDR" or rates=="KRW" or rates=="JPY" or rates=="INR":
        print(value,FC,"=",round(d[rates]*float(value),2),rates)
"""
print(value,FC,"=",round(c.convert(FC,"USD",int(value)),2),"USD")
print(value,FC,"=",round(c.convert(FC,"EUR",int(value)),2),"EUR")
print(value,FC,"=",round(c.convert(FC,"INR",int(value)),2),"INR")
print(value,FC,"=",round(c.convert(FC,"THB",int(value)),2),"THB")
print(value,FC,"=",round(c.convert(FC,"IDR",int(value)),2),"IDR")
print(value,FC,"=",round(c.convert(FC,"KRW",int(value)),2),"KRW")
print(value,FC,"=",round(c.convert(FC,"JPY",int(value)),2),"JPY")
"""
while True:
    try:
        if keyboard.is_pressed('ENTER'):
            print("you pressed Enter, so printing the list..")
            print(a)
            break
        if keyboard.is_pressed('Esc'):
            print("\nyou pressed Esc, so exiting...")
            sys.exit(0)
    except:
        break


