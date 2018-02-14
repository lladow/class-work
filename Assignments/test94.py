fname = input("Enter file name: ")
fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.split()
    if not len(words) == 0 and words[0] == 'From' :
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1
most = counts.keys()
for key in most:
    if counts[key] == max(counts.values()):
        print(key, counts[key])