requested_number = int(input("Enter number from 1 to 1000: "))


if requested_number <= 0 or requested_number > 1000:
    print("Please choose number from a given range ")
else:
    while requested_number != 1:
        print(int(requested_number), end = " -> ")
        if requested_number % 2 == 0:
            requested_number = requested_number*0.5
        elif requested_number % 2 == 1:
            requested_number = requested_number*3 + 1
    print(1)