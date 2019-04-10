numbers = [5,7,6,1,9,2,8,4,3]
diveNums = []
total = []

x = True
i = 0
while x == True :
    i = i+1
    if len(numbers)%2 == 0 :
        for num in range( (int (len(numbers) /2)) ) :
            diveNums.append(numbers.pop(num))

    else :
        for num in range( (int (len(numbers) /2)) + 1 ) :
            diveNums.append(numbers.pop(num))

    total.append(diveNums)
    diveNums = []
    # if num+1 == len(numbers) :
    print(i)
    print(total)
    if len(numbers) == 0 :
        x = False
