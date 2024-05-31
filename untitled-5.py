# add_2 = lambda x: return x + 2
a = (lambda x: x + 2)(2)
print(a)

# add_2 = lambda x: x + 2
add_2 = lambda x, y, z: x + y + z + 2

print(add_2)
print(add_2(3, 5, 8))

full_name = lambda first_name, last_name: first_name + " " + last_name
