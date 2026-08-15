#prices 

#price = Small pizza: $15, Medium pizza: $20, Large pizza: $25)
#Add pepperoni for Small pizza: +$2, Medium or Large pizza: +$3
#Add extra cheese for any pizza: +$1


size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
Extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
        if Extra_cheese == "Y":
            bill += 1
elif size == "M": 
    bill = 20
    if pepperoni == "Y":
        bill += 3
        if Extra_cheese == "Y":
            bill += 1


elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
        if Extra_cheese == "Y":
            bill += 1
print(f"Your final bill is: ${bill}.")
