name = input("Enter your name: ")

try:
    res = any(char.isdigit() for char in name)
    if res:
        # raise Exception("Number input is not accepted!")
        raise ValueError("Number input is not accepted!")
    # print("An error occurred")
# except Exception as e:
except ValueError as e:
    print(f"Error {e}")
else:
    print(f"Hello {name}")
