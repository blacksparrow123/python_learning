import string
from pprint import pprint

#string.ascii_lowercase string.ascii_uppercase

upperDict = dict(zip(string.ascii_lowercase, string.ascii_uppercase))

def getUppercase(line):
  upperLine = ''
  
  for letter in line:
    if letter in upperDict:
      upperLine += upperDict[letter]
    else:
      upperLine += letter
  return upperLine
  
assert getUppercase('Hello') == 'HELLO'

assert getUppercase('hello') == 'HELLO'

assert getUppercase('HELLO') == 'HELLO'

assert getUppercase('Hello, world!') == 'HELLO, WORLD!'

assert getUppercase('goodbye 123!') == 'GOODBYE 123!'

assert getUppercase('12345') == '12345'

assert getUppercase('') == ''
