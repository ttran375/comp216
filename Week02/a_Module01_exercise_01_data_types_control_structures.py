#imports and variables
from random import randint

#the following variable will be used in the rest of the exercise
pm = 'justin pierre james trudeau'
instructor = 'narendra pershad'
harry = "You've gotta ask yourself a question: do I feel lucky? …well, do ya, punk?"
numbers = [randint(5, 10) for _ in range(20)]


#use the following dictionary for your exercises
d = {
    3462: 'Artificial Intelligence',
    3468: 'Software Engineering Technician',
    3469: 'Software Engineering Technology',
    3472: 'Artificial Intelligence (FT)',
    3478: 'Software Engineering Technician (FT)',
    3528: 'Health Informatics Technology (FT)',
    3609: 'Game - Programming',
    3668: 'Health Informatics Technology',
    3679: 'Game - Programming (FT)'}


# - 1 mark
# display the dictionary
print(d)


# - 1 mark
# use the keys() and values() method to display the keys and values
print(d.keys())
print(d.values())
print(d.items())

value_ind_1 = list(d.keys())[1]
print(value_ind_1)
unique_values = set(d.values())


# - 2 mark
# Use the key-index technique to retrieve the name of program 3462
# Use the get() method to retrieve the name of program 3462
# It there a difference? Yes or No -- Explain

print(d[3462])
print(d.get(3462))

# print(d[4462])
print(d.get(4462, False))

d[3479] = 'Networking and Data Centers'
print(d)
d[3479] = 'IoT Engineering'
print(d)

d.pop(3468)
print(d)

d.pop(4500, 'No Key')
print(d)

d.popitem()
print(d)

d2 = {4251: 'System Architecture', 2356: 'UX Design'} # Try to create a list of tuples [(4251, 'System Architectures), (2356, 'UX Design')]
d.update(d2)
print(d)
#d.clear()
