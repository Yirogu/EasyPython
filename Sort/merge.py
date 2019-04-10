numbers = [5,7,6,1,9,2,8,4,5]
diveNums = []
total = []

x = True
i = 0
while x == True :
    i = i+1
    if len(numbers)%2 == 0 :
        for num in range( (int (len(numbers) /2)) ) :
            diveNums.append(numbers.pop(0))


    else :
        for num in range( (int (len(numbers) /2)) + 1 ) :
            diveNums.append(numbers.pop(0))

    total.append(diveNums)
    diveNums = []

    for num in range(len(numbers)) :
            diveNums.append(numbers.pop(0))



    total.append(diveNums)
    diveNums = []



    # if num+1 == len(numbers) :
    print(i)
    print(total)
    x = False
