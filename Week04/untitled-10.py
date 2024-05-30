try:
    file = open('abc.txt', 'r')
except IOError as err:
    print(f'File is not found!')
except ValueError as err:
    print(f'Wrong value passed in open function')
except Exception as e:
    print(f'Error has ocurred -- Details: {e}')
else:
    print('File is read')
finally:
    print('Terminated program')