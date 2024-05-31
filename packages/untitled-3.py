x = 'variable_1'    #Global
def f():
  x = 'variable_2'  #Enclosing
  def g():
    print(x)  #Local
  g()
f()
