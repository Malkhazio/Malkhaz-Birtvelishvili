number = int(input("Enter number: "))

my_list = [0, 1]
for i in range(2, number+1):
    my_list.append(my_list[i-2]+my_list[i-1])
print(my_list[-1])