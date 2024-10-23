from pathlib import Path
import json

def ask_fav_number(path):
  number = input("Please entet Your favorite number.\n")
  content = json.dumps(number)
  path.write_text(content)
  return number
  
def read_fav_number(path):
  content = path.read_text()
  number = json.loads(content)
  return number
  
path = Path('fav_number.json')
if path.exists():
  number = read_fav_number(path)
  print(f"Your favorite number is {number}!")
else:
  number = ask_fav_number(path)
  print(f"Number {number} was stored in {path}!")