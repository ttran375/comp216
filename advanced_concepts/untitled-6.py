# def to_fahrenheit(c):
#     return


# celc_temps = [100, 40, 60, 20]

# for temp in celc_temps:
#     print(to_fahrenheit(temp))ƒ

celc_temps = [100, 40, 60, 20]
fah_temp = []

for temp in celc_temps:
    fah_temp.append(9 / 5 * temp + 32)


def convert_to_fahr(c):
    return 9 / 5 * c + 32


fhar_list_2 = map(convert_to_fahr, celc_temps)
print(list(fhar_list_2))


###### --> pow(x, y) --> x ** y
# output = map(pow, (6, 9, 4, 3), [2, 6, 0, 1], [5, 7, 0, 4])
output = map(pow, (6, 9, 4, 3), [2, 6])
print(list(output))
