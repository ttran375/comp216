# Basic arithmetic operations
result1 = 4 + 5
result2 = 89 - 4.3
a = 3 * 4
a = 12
print(f"value of a is {a}")
print("Type of a:", type(a))
print("Attributes of a:", dir(a))
print("Help on a:", help(a))

# Type conversion
int_num = int(3.14)
float_num = float(5)
complex_num = complex(3)
complex_num2 = complex(1, 2)

# Boolean operations
bool_true = bool("true")
bool_false = bool("False")
bool_other = bool("lkjlk")
bool_empty_str = bool("")
bool_int = bool(89)
bool_zero = bool(0)
bool_empty_list = bool([])

# String operations
str1 = "Hello world"
str2 = "Narendra's toys"
str3 = """First line
Second line"""
byte_str = b"First line"
unicode_char1 = "\u00c4\u00e8"
unicode_char2 = "\U000000c4\U000000e8"
a = "the quick brown fox jumps over the lazy dog"
split_words = a.split()
upper_case = a.upper()
capitalized = a.capitalize()
title_case = a.title()
replaced = a.replace("o", "O")
find_dog = a.find("dog")

# Tuple, List, Set, and Dictionary operations
tup1 = ()
tup2 = ("programming", "mathematics", 2018, 3.14)
tup3 = (1, 2, 3, 4, 5, 3, 2, 1)
lst1 = []
lst2 = ["programming", "mathematics", 2018, 3.14]
lst3 = [1, 2, 3, 4, 5, 3, 2, 1]
set1 = set()
set2 = {"programming", "mathematics", 2018, 3.14}
set3 = {1, 2, 3, 4, 5, 3, 2, 1}
dict1 = {"Ilia": "red", "Narendra": "green", "Arben": "blue"}
dict1_value = dict1["Narendra"]
dict1["Devaraja"] = "red"
dict1["Ilia"] = "orange"
del dict1["Ilia"]

# Conditional statements
temp = 98
if temp < 98:
    temp = 98

number = 5
if number >= 0:
    print("+")
