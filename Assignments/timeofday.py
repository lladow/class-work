fname = input("Enter file name: ")
fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.split()
    if not len(words) == 0 and words[0] == 'From' :
        d1, d2, d3 = words[5].split(':')
        if d1 not in counts:
            counts[d1] = 1
        else:
            counts[d1] += 1
most = list()
for val, key in counts.items():
    most.append( (val, key) )
most.sort()
for key, val in most : 
    print(key, val)
