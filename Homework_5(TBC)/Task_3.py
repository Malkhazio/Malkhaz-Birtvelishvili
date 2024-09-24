'''
end="": No separator, prints output continuously.
end=" ": Single space separator between outputs.
end="\n": Default, newline between outputs.
end="\t": Tab space separator between outputs.
end=", ": Comma and space separator.
end="---": Custom separator (e.g., ---).
end="\n\n": Double newline for extra spacing.
'''

nat_number = int(input("Pick a number from 0 to 20: "))
if nat_number < 0 or nat_number > 20:
    print("Please enter number from a given range!")
else:
    a, b = 0, 1
    just_number = 0
    print(a, end= " ")
    while just_number <= nat_number:
        print(b, end = " ")
        a, b = b, a + b
        just_number += 1

