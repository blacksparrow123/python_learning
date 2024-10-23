from pathlib import Path

def count_words(path):
  """Count the approximate number of words in file."""
  try:
    contents = path.read_text(encoding='utf-8')
  except FileNotFoundError:
    #print(f"Sorry, the file {path} does not exist.")
    pass
  else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
  path = Path(filename)
  count_words(path)