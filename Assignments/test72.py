fname = input('Enter file name: ')
fhand = open(fname)
total = 0.0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        vline = float(line[20:])
        total = total + vline
        count = count + 1
print("Average spam confidence: ", total/count)