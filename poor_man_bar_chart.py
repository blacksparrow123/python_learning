from pprint import pprint
from collections import defaultdict

sentence = "a quick brown fox jumps on a lazy dog"
occurance_dict = defaultdict(list)
for letter in sentence.lower():
    if letter == " ":
        continue
    occurance_dict[letter] += letter

pprint(occurance_dict)
