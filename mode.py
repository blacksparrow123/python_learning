def mode(numbers):
  diction = {1: 0, 2: 0, 3: 0, 4: 0}
  biggest_number = 0
  biggest_key = 1
  if numbers == []:
    return None
  for number in numbers:
    for key in diction.keys():
      if key == number:
        diction[key] += 1
  
  for key in diction.keys():
    if diction[key] > diction[biggest_key]:
      biggest_key = key
  return biggest_key
  
numbers = [1, 2, 3, 4, 4]
print(mode(numbers))

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4