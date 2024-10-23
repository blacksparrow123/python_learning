from pathlib import Path

path = Path("programming.txt")

names = ''
i = 0
while i < 3:
  name= input("Please enter Your name: \n")
  names += name + '\n'
  i += 1

path.write_text(names)