speed = int(input("რამდენი კმ/სთ-ით მოძრაობს მანქანა? "))

if speed > 120:
     print("VERY FAST")
elif speed > 60:
     print("FAST")
elif speed > 30:
     print("MODERATE")
elif speed > 0:
     print("SLOW")
else:
    print("incorrect input")
