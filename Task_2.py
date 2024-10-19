w1 = input(str("Enter the first word: "))
w2 = input(str("Enter the second word: "))
for i in range(len(w1)):
    if w1[i] in w2:
        w2 = w2.replace(w1[i], "")
        if len(w2) == 0:
            print("YES")
    else:
        print("NO")
        break