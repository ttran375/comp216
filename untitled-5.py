# add_2 = lambda x: return x + 2
a = (lambda x: x + 2)(2)
print(a)

# add_2 = lambda x: x + 2
add_2 = lambda x, y, z: x + y + z + 2

print(add_2)
print(add_2(3, 5, 8))

full_name = lambda fn, ln: f"Full Name of User: {fn.upper()} {ln.upper()}"
field_1 = "Bob"
field_2 = "Wells"

print(full_name(field_1, field_2))


basic_fn = lambda func, a: a + func(a)
nest_lambda = basic_fn(lambda a: a**3, 3)
# nest_lambda = basic_fn(lambda a: a/0, 3)
print(nest_lambda)
