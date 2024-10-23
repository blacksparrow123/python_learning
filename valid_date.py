def isLeapYear(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False

def isValidDate(year, month, day):
  if  0 < month <= 12 and 0 < day:
    if isLeapYear(year) and month == 2 and day == 29:
      return True
    if month == 2 and not (day <= 28):
      return False
    elif month in [4,6,9,11] and not (day <= 30):
      return False
    elif month in [1,3,5,6,7,10,12] and not (day <= 31):
      return False
    else:
      return True
  else:
    return False
    
assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

 

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay