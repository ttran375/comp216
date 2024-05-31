new_list = []

for num in range(20):
    if num % 2 == 0:
        new_value = num**2
        new_list.append(new_value)

print(new_list)


new_list_2 = [num_value**2 for num_value in range(20) if num_value % 2 == 0]
print(new_list_2)
