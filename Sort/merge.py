numbers = [5,7,6,1,9,2,8,4,3]
diveNums = []
x = True
while x == True :
    if len(numbers)%2 == 0 :
        for num in range( (int (len(numbers) /2)) ) :
            print(num)

    else :
        for num in range( (int (len(numbers) /2)) + 1 ) :
            print(num)

    # if num+1 == len(numbers) :
    x = False
