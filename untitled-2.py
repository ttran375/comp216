sentence = "COMP216 is a networking course at Centennial College!"

vowel = "aeiou"
other = "1234567890 .?!"

const_in_sent = []

for char in sentence:
    if char.lower() not in vowel and char not in other:
        const_in_sent.append(char)

print(const_in_sent)

const_2 = [char for char in sentence if char.lower() not in vowel and char not in other]
print(const_2)


def const_validator(char_input):
    if char_input.lower() not in vowel and char_input not in other:
        return True
    else:
        return False


const_3 = [char for char in sentence if const_validator(char)]
print(const_3)
