fname = input('Enter file name: ')
fhand = open(fname)
for line in fhand:
    sline = line.strip()
    print(sline.upper())