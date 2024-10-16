my_word = input(str("Please enter text: "))

for i in range(2,len(my_word)):
    if my_word[i] != "e" and i % 2 == 0:
        print(my_word[i])