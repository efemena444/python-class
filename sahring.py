bill = float(input("What was your bill? "))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people are splitting the bill? "))
tipaspercent = tip / 100
totalTip = bill * tipaspercent
totalbill = bill + totalTip
#billperperson = totalbill / people
#finalamount = round(billperperson, 2)
print(f"person should pay {totalbill}")
      