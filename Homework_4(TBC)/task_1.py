import random
first_dice = [1, 2, 3, 4, 5, 6]
second_dice = [1, 2, 3, 4, 5, 6]
num_of_players = int(input("Enter players number: "))

for player in range(num_of_players):
    print(random.choice(first_dice), random.choice(second_dice))