import string
word = input(str("Please enter text: "))
word = word.translate(str.maketrans('', '', string.punctuation))
word = word.replace(" ", "")
left = 0
right = len(word) - 1
while left <= right:
    if word[left] == word[right]:
        left += 1
        right -= 1
        if right - left <= 1:
            print("Is Palindrome")
            break
    else:
        print("Not a palindrome")
        break
