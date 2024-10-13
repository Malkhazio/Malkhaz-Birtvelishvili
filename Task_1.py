import random
requested_number = int(input("Enter number from 0 to 100: "))

num = 0


if requested_number < 0 or requested_number > 100:
    print("Please choose number from a given range ")
else:

    while num < 10 :
        num += 1
        comp_num = random.randint(0, 100)
        if requested_number > comp_num:
            print("high")
        if requested_number < comp_num:
            print("low")            
        if comp_num == requested_number:
            print("You are winner")
            break    
if num == 10 and requested_number != comp_num:
    print("Computer is winner")
