import random

number = int(input("Enter how many random numbers from 1 to 1000 do you want appear on the terminal? maximum amount is 29:     "))
my_max_number = 0
if number <= 0 or number > 29:
    print("invalid number")
else:  
    for i in range(number):
            temp = random.randint(0, 1000)
            print(temp)
            if temp > my_max_number:
                my_max_number = temp
    print("maximum random number was: " + str(my_max_number))
    