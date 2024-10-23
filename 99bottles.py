

for i in range(99,1,-1):
  print(
  ''' ''',i, '''bottles of beer on the wall,\n'''
  ''' ''',i, '''bottles of beer,
  Take one down,
  Pass it around,\n'''
  ''' ''',i-1,'''bottles of beer on the wall,
  '''
  )
  if i == 2:
    print('''
1 bottle of beer on the wall,
1 bottle of beer,
Take one down,
Pass it around,
No more bottles of beer on the wall!
'''
      )
    