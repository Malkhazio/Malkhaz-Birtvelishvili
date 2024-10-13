reqst_number = int(input("Enter number from 1 to 10000: "))
reversed_reqst_number = str(reqst_number)[: :-1]
sum_of_digits = sum(int(i) for i in str(reqst_number))
if reqst_number < 0 or reqst_number >= 10000:
    print("Please choose number from a given range ")
else:
    print(f"Entered number: {reqst_number}")
    print(f"Requested number: {reversed_reqst_number}")
    print(f"Sum of digits: {sum_of_digits}")