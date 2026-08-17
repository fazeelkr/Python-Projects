import random   

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'   ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



nr_number = input("how many numbers would you like in your password? ")
nr_symbols = input("how many symbols would you like? ")
nr_letters = input("how many letters would you like? ")


nr_letters = int(nr_letters)
nr_symbols = int(nr_symbols)
nr_number = int(nr_number)


number_of_letters = random.choices(letters, k=nr_letters)
number_of_symbols = random.choices(symbols, k=nr_symbols)   
number_of_numbers = random.choices(numbers, k=nr_number)    


your_password = ''.join(number_of_letters) + ''.join(number_of_symbols) + ''.join(number_of_numbers)
print (your_password)