def printHandshakes(names):
  lenLst = len(names)
  numberShakes = 0
  for i in range(lenLst):
    for n in range(i+1, lenLst):
      print(f"{names[i]} shakes hands with {names[n]}")
      numberShakes += 1
  return numberShakes
      
printHandshakes(['Alice', 'Bob'])

assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3

assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

