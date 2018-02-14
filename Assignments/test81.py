def chop(t):
    del t[len(t)-1]
    del t[0]

letters = ['a', 'b', 'c', 'd', 'e', 'f']
chop(letters)
print(letters)

def middle(s):
    return s[1:len(s)-1]

letters = ['a', 'b', 'c', 'd', 'e', 'f']
allbut = middle(letters)
print(allbut)
print(letters)


