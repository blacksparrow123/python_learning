
def drawRectangle(width, heght):
  for row in range(heght):
    for column in range(width):
      print('#', end='')
    print('\n')
  
drawRectangle(10, 7)