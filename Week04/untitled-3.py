x = "variable_1"  # Global


def f():
    x = "variable_2"  # Enclosing

    def g():
        global x
        print(x)  # Local
        # print(locals())

        # print(global x)  # Local
        # print(locals())

    g()
    # print(locals())


f()

# print(globals())
