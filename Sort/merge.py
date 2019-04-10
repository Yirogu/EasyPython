numbers = [5,7,6,1,9,2,8,4,3]
diveNums = []
x = True
i = 0
while x == True :
    i = i+1
    if len(numbers)%2 == 0 :
        for num in range( (int (len(numbers) /2)) ) :
            diveNums[i]

    else :
        for num in range( (int (len(numbers) /2)) + 1 ) :
            print(num)

    # if num+1 == len(numbers) :
    x = False
