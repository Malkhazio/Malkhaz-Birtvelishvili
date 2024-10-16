my_word = input(str("Please enter text: "))
count = 0
if len(my_word) % 2 == 0:
    print(my_word[int(len(my_word)/2-1)], my_word[int(len(my_word)/2)])
else:
    while count < 5:
        print(my_word[0], my_word[int(len(my_word)/2)], my_word[-1])
        count += 1