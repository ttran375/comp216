# try:
#     file = open("text.txt", "r")
# except:
#     print("An error occurred")

# file = open("text.txt", "r")

try:
    file = open("text.txt", "r")
    # file = open("text.txt", "rrrrrr")
except IOError as err:
    print(f"File is not found -- Details: {err}")
except ValueError as err:
    print(f"Wrong value passed in open function {err}")
except Exception as e:
    # print("An error occurred -- Details: {e}")
    print("Error has occured -- Details: {e}")
else:
    print("file is read")
finally:
    print("Terminated program")
