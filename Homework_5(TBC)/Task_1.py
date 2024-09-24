nat_number = int(input("Enter number from 0 to 50: "))


number = 0

if nat_number < 0 or nat_number > 50:
    print("Please choose number from a given range ")
else:

    while nat_number > number:
        number += 1
        dividers = [] 
        for i in range(1, 51):
            if number % i == 0:  
                dividers.append(i)
                if len(dividers) == 3:
                    break
        print(f"{number} - {dividers}")

    