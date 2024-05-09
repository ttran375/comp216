## String

a = 'Hello world'
a
a = "Narendra's toys"
a
a = '''First line
a
a = b'First line'
a
type(a)
list(a) # byte string to list
list('First line') # normal string to list
a = '\u00c4\u00e8' #4 hex digits for one character
a
a = '\U000000c4\U000000e8' #8 hex digits for one character
a
ord(a[0]) #returns an integer for the Unicode character
chr(196) #converts an integer to its Unicode character
a = 'the quick brown fox jumps over the lazy dog'
a.split()
a.upper()
a = 'the quick brown fox jumps over the lazy dog'
a.split()
a.upper()
a = 'the quick brown fox jumps over the lazy dog'
a.capitalize()
a.title()
a = 'the quick brown fox jumps over the lazy dog'
a.capitalize()
a.title()
a = 'the quick brown fox jumps over the lazy dog'
a.replace('o', 'O')
a.replace('o', 'O').swapcase()
a = 'the quick brown fox jumps over the lazy dog'
a.replace('o', 'O')
a.replace('o', 'O').swapcase()
a = 'the quick brown fox jumps over the lazy dog'
a.find('dog')
a = 'the quick brown fox jumps over the lazy dog'
a.find('dog')