from random import randint

def rollDice(amount_of_rolls):
  sum = 0
  for i in range(amount_of_rolls):
    side = randint(1,6)
    sum += side
  return sum

print(rollDice(100))    
assert rollDice(0) == 0

assert rollDice(1000) != rollDice(1000)

for i in range(1000):

    assert 1 <= rollDice(1) <= 6

    assert 2 <= rollDice(2) <= 12

    assert 3 <= rollDice(3) <= 18

    assert 100 <= rollDice(100) <= 600