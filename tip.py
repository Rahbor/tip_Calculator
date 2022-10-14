print("Welcome To Tip Calculator!\n")
price =float(input("Price: $"))
tip = int(input("What percentage would you like to give? 10, 12 or 15 ? "))
persons= int(input("How many people aterer to split the bill? "))
tipp = price * (tip/100)
total = (price + tipp)/persons
x= round(total,2)
print(f"Each person should pay: {x}$")
