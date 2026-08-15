#prices 

#price = Small pizza: $15, Medium pizza: $20, Large pizza: $25)
#Add pepperoni for Small pizza: +$2, Medium or Large pizza: +$3
#Add extra cheese for any pizza: +$1


size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
Extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have entered the wrong input")

if pepperoni =="Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if Extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
    