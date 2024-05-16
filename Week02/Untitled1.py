# Conditional/Branching

temp_1 = temp_2 = 21

if temp_1 > 20:
    print("warm")
else:
    print("cold")


# Operators
print(2 == 2.000000)
print(2 == "2")
# print(2 < '3') --> Type Error

a = 0.1 + 0.2
print(a)
print(a == 0.3)
from math import isclose

print(isclose(a, 0.3))

print("A" < "a")

print([1, 2, 3, 4] != [2, 3, 4, 5])

print([1, 2, 3, 4] != [1, 2, 3, 5])
print([1, 2, 3, 4] <= [1, 2, 3, 5])
print([1, 2, 3, 4] <= [0])

print(3.14 < 5.56 and 5.6 == 5.60)

a = 1 + 2
b = 3 + 1
c = 0
print(a and b)
print(a and c)
print(b and c)
print(a or b)
print(c and [])
print(c or [])

num_1 = 2024
num_2 = 2024

print(num_1 == num_2)
print(num_1 is num_2)


weight = 150

if weight < 100:
    print("under weight")
    print("see Dietitian")
elif weight < 140:
    print("appr. weight")
elif weight < 180:
    print("concerning weight")
else:
    print("!!!!")


weight = 150
age = 12

if weight < 100 and age > 20:
    print("under weight")
    print("see Dietitian")
elif weight < 140 and age > 30:
    print("appr. weight")
elif weight < 180 and age > 40:
    print("converning weight")
else:
    print("!!!!")


weight = 150
age = 12

if weight < 100 and age > 20 or ...:
    print("under weight")
    print("see Dietitian")
elif weight < 140 and age > 30:
    print("appr. weight")
elif weight < 180 and age > 40:
    print("converning weight")
else:
    print("!!!!")


weight_2 = 90
if weight_2 < 100:
    print("under weight")
    print("see Dietitian")

"EXPR1 if CONDITION else EXPR2"
age = 12
if age < 13:
    print("elementary")
else:
    print("highschool")

status = "elementary" if age < 13 else "highschool"
print(status)

x = 0
sample = "foo" if x == 1 else "bar" if x == 2 else "baz" if x == 3 else "quz"
print(sample)


# While Loops

n = 10
while n > 0:
    print(n)
    n -= 1

sample_list = [34234, 12643, 89768, 23412]
while sample_list:
    a = sample_list.pop(-1)
    print(a)
    print(sample_list)


sample_list = [34234, 12642, 89768, 23412, 4651234, 886712]
while sample_list:
    a = sample_list.pop(-1)
    if a % 2 == 1:
        print("odd value")
        break
    print(a)
    print(sample_list)
else:
    print("All values are even")

print("Program Terminated")


sample_list = [34234, 12642, 89769, 23412, 4651234, 886712]
while sample_list:
    a = sample_list.pop(-1)
    if a % 2 == 1:
        print("odd value")
        continue
    print(a)
    print(sample_list)
else:
    print("All values are even")

print("Program Terminated")


# For Loop
num_line = [24, 67, 12, 40, 74]

for num in num_line:
    print(num)

num_iter = iter(num_line)
print(num_iter)


# For Loop
num_line = [24, 67, 12, 40, 74]

num_iter = iter(num_line)
print(num_iter)
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
# print(next(num_iter))


d = {1:'a', 2:'b', 3:'c', 4:'d'}
for item in d:
  print(item)
for item in d:
  print(d[item])


for k,v in d.items():
  print(f'Key: {k} --> Value: {v}')
