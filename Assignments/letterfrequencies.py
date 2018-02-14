fname = input("Enter file name: ")
fhand = open(fname)
letters = dict()
for line in fhand:
    line = line.lower()
    for x in line:
        if x not in 'abcdefghijklmnopqrstuvwxyz' : continue
        if x not in letters:
            letters[x] = 1
        else:
            letters[x] += 1
most = list()
for key, val in letters.items():
    most.append( (val, key) )
most.sort(reverse = True)

for key, val in most :
    print(key, val)
