import datetime
birth_year = int(input("მიუთითეთ თქვენი დაბადების წელი: "))
birth_month = int(input("მიუთითეთ მერამდენე თვეში ხართ დაბადებული: "))
birth_day = int(input("მიუთითეთ რომელ რიცხვში დაიბადეთ: "))

original_date = datetime.datetime(birth_year, birth_month, birth_day)

weekday_number = original_date.weekday()

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day_name = days_of_week[weekday_number]

print(day_name)