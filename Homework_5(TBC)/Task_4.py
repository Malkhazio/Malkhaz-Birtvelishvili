#4. დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n, სადაც 0 < n < 50. 
#Პროგრამამ უნდა დახატოს n სიმაღლის ნაძვის ხე სიმბოლოებით *, /, | და \ .

height = int(input("Please enter height of the tree: "))
print(" " * (height + 1 ) + "*")
for i in range(height -1):
    print(" " * (height - i ) + (i + 1) * "/"+ "|" + (i + 1) * "\\")
print(" " * (height + 1 ) + "|")