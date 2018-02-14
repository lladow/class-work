fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print("File not found: ", fname)
    quit()
count = 0
try:
    for line in fhand:
        words = line.split()
        if not len(words) == 0 and words[0] == "From" :
            print(words[1])
            count = count + 1
except:
    print("File: ", fname, "contains no data.")
    quit()

print("There were", count, "lines in the file with From as the first word.")