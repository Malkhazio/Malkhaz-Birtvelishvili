first_number = int(input("დაწერე პირველი რიცხვი: "))
second_number = int(input("დაწერე მეორე რიცხვი: "))

division = first_number % second_number

if division == 0 and first_number > 0 and second_number > 0:
    print("პირველი რიცხვი მეორეს ჯერადია")
else:
    print("პირველი რიცხვი არ არის მეორეს ჯერადი")