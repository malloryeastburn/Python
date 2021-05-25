catNames = []
while (True):
    print('Enter a cat name:')
    name = input()
    if name == '':
        break
    else:
        catNames += [name]
print('The catn names are:')
for name in catNames:
    print('    ' + name)
