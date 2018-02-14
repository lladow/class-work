total = 0
count = 0

while True:
    test = input("Enter a number:")

    if test == 'done':
        break
    try:    
        num = float(test)

    except:
        print ("Invalid input")
        continue
    total = total + num
    count = count + 1

print ("")
print ("Sum is:", total)
print ("Count is:", count)
print ("Average is:", total/count)


