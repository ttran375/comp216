import calc
import importlib

output_1 = calc.add(4,7)
print(output_1)

output_2 = calc.diff(2,9)
print(output_2)

importlib.reload(calc)

print(globals())
