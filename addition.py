while True:
  try:
    x = input("Please enter a first number")
    x = int(x)
  
    y = input("Please enter a second number")
    y = int(y)
  except ValueError:
    print("Please enter a digit")
  else:
    print(x + y)