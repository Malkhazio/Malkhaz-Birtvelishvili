# Value of n
n_values = [10, 100, 10000, 100000]

for n in n_values:
    x = 0
    sign = 1
    for i in range(1, 2*n, 2):
        x += sign * (1/i)
        sign *= -1
    x *= 4
    print(f"For n = {n}, x = {x}")
