from pprint import pprint


list = [3, 7, 10, 4, 1, 9, 6, 2, 8]

list.sort()

lenList = len(list)

if lenList % 2 == 1:
    pprint(list[lenList // 2])

print(list[:])
