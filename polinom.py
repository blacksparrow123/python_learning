import sys

def load(file):
  try:
    with open(file) as in_file:
      loaded_txt = in_file.read().strip().split('\n')
      loaded_txt = [x.lower() for x in loaded_txt]
      return loaded_txt
  except IOError as e:
    print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
  sys.exit(1)
  
word_list = load("dct.txt")
pali_list = []
for word in word_list:
  if len(word) > 1 and word == word[::-1]:
    pali_list.append(word)
    
print("\nNumber of palidromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')