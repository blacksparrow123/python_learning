from pathlib import Path


def word_count(files):
    for file in files:
        path = Path(file)
        content = path.read_text()
        content = content.lower()
        print(content.count("work"))


files = ["pg61.txt"]
word_count(files)
