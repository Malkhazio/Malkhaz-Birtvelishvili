dividers = []

number = int(input("Enter the number from 0 to 1000: "))
if number <= 0 or number > 1000:
    print("Enter number from the given range")
else:
    for i in range(1, number + 1):
        if number % i  == 0:
            dividers.append(i)
    print(dividers)    