from pathlib import Path

files = ['cats.txt', 'dogs.txt', 'snakes.txt']

try:
    for file in files:
        path = Path(file)
        contents = path.read_text()
        print(contents)
except FileNotFoundError:
    pass