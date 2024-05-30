# print(dir(__builtins__))
x = 'variable_1'
def f():
    x = 'variable_2'

    def g():
        x = 'variable_3'


print(x)
print(globals())
