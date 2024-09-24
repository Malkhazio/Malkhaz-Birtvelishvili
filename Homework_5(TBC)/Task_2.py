

for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} * {i} = {j*i}", end = "\t")
    print()


'''
end="": No separator, prints output continuously.
end=" ": Single space separator between outputs.
end="\n": Default, newline between outputs.
end="\t": Tab space separator between outputs.
end=", ": Comma and space separator.
end="---": Custom separator (e.g., ---).
end="\n\n": Double newline for extra spacing.
'''