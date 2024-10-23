import json
import os 

data = {'name': 'Eric', 'age': 38 }
path="/storage/emulated/0/termux"
cwd = os.getcwd()
print(cwd)
os.chdir(path)
print(cwd)

with open('./test.json', 'w') as f:
    json.dump(data, f, indent=4)


