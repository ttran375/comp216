import importlib
# import calc as c
import calc

print(globals)

# output_1 = c.add(4, 7)
# print(output_1)

# output_2 = c.diff(2, 9)
# print(output_2)

print(globals)

importlib.reload(calc)
# import calc
# import calc

print(globals())
