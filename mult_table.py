header = ['   |  1'] + [str(n).rjust(5) for n in range(2,11)]
header = ''.join(header)
separetor = ['---'] + ['+'] + ['-'.rjust(5,'-') for n in range(1,11)]
separetor = ''.join(separetor)

print(header)
print(separetor)

for row in range(1,11):
  print(str(row).rjust(3), end='|')
  for column in range(1,11):
    print(str(column*row).rjust(3) + ' ',end=' ')
  print('\n')


