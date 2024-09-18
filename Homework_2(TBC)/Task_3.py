number = int(input("აირჩიე ნებისმიერი მთელი რიცხვი 2-დან 10-ის ჩათვლით: "))
if number < 2 or number > 10:
    print("რიცხვი არ ხვდება მითითებულ არეალში")
else:
    martivi_ricxvebi = [2, 3, 5, 7]
    gamyofebi = []
    for i in martivi_ricxvebi:
        if number % i == 0:
         gamyofebi.append(i)

    print(gamyofebi)