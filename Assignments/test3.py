
def computepay(hours, rate):
    if hours > 40:
        pay = rate * 40 
        overtime = hours % 40 * (rate * 1.5)
        result = pay + overtime
    else:
        result = hours * rate
    
    return result

def getinput():
    try:    
        hours = float(input('Enter hours:'))
        rate = float(input('Enter rate:'))

        print ('Pay: $', computepay (hours, rate))
    except:
        print ("Bad Input!")
        getinput()

getinput()
