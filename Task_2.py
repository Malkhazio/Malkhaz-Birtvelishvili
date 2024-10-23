import random
import math
n_values = [10, 100, 100000, 10000000]

for n in n_values:
    counter = 0
    count = 0
    
    while count < n:
        a = random.random()
        b = random.random()
        if math.sqrt(a ** 2 + b ** 2) <= 1:
            counter += 1
        count += 1
    
    result = 4 * counter / n
    print(f"For n = {n}, result = {result}")
print("As n gets close to infinity result converges into π. It took about 10 second to print final result.")