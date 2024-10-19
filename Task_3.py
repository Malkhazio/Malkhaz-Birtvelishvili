date = input(str("Enter a date: "))
year = date[:4]
month = date[5:7]
day = date[8:10]
hour = date[11:13]
minute = date[14:16]
second = date[17:19]
hour = str(int(hour) % 12 or 12)
timezone = int(date[-5:-3])
output = f"{day}-{month}-{year} {hour}:{minute}:{second}+{timezone}"

print(output)
