import string
from pprint import pprint

#string.ascii_lowercase string.ascii_uppercase

upperDict = dict(zip(string.ascii_lowercase, string.ascii_uppercase))

pprint(upperDict['m'])
