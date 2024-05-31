name = input('Enter your name: ')

try:
    res = any(char.isdigit() for char in name)
    if res:
        raise ValueError('Number input is not accepted!')
except ValueError as e:
    print(f'Error: {e}')
else:
    print(f'Hello {name}')