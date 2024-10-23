
def drawBorder(height, width):
  line = '+' + '-' * (width - 2) + '+'
  sides = '|' + ' ' * (width - 2) + '|'

  print(line)
  for i in range(height - 2):
    print(sides)
  print(line)

height = input("Height:\n")
width = input("Width:\n")
drawBorder(int(height),int(width))
  