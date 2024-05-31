data_input = [("a", 1), ("B", 2.000), ("c", 3.0), ("D", 4)]

clean_dict = dict()

# for item in data_input:
#     print(item)

for key, value in data_input:
    print(key, value)
    clean_dict[key] = value

for key, value in data_input:
    clean_dict[key.upper()] = value * 1.0

print(clean_dict)

clean_dict_2 = {key.upper(): value * 1.0 for key, value in data_input}
print(clean_dict_2)
