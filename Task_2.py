my_word = input(str("Please enter text: "))

for i in range(len(my_word)):
    if my_word[i] not in ["a", "e", "i", "o", "u", "A", 'E', 'I', 'O', 'U']:
        print(my_word[i])
