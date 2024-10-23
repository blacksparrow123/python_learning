import string, random

def generatePassword(length):
  if length < 12:
    length = 12
  pw = ''
  SPECIAL = '~!@#$%^&*()_+'
  passwrdString = string.ascii_lowercase + string.ascii_uppercase + string.digits + SPECIAL
  passwrdString = list(passwrdString)
  random.shuffle(passwrdString)
  
  for i in range(length):
    pw += passwrdString[i]
    pw = ''.join(pw)
  
  return pw
  
print(generatePassword(10))