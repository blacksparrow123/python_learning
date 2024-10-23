from pathlib import Path
import json

def store_data(path):
  for data, content in user_data.items():
    user_data[data] = input(f"Please enter Your {data}.\n")
  storage = json.dumps(user_data)
  path.write_text(storage)

def read_data(path):
  storage = path.read_text()
  storage = json.loads(storage)
  for data, content in storage.items():
    print(f"{data}: {content}")
    
path = Path('user_info.json')
user_data = {'username':'', 'age':'', 'years_of_work':''}

if path.exists():
  read_data(path)
else:
  store_data(path)