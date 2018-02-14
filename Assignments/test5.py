def getinput(total, total_values):

    input_value = input('Enter a number:')

    if input_value != 'done':
        try:    
            input_number = float(input_value)
            total += input_number
            total_values += 1
            getinput(total, total_values)

        except:
            print ("Invalid input")
            getinput(total, total_values)
    else:
         print(int(total), total_values, (total / total_values))

total = 0
total_values = 0

getinput(total, total_values)
