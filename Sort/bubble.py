numbers =[3,2,4,3,1,2,0]


for num in range(len(numbers)):
    print(f"step {num +1} result {numbers}")
    tmp = numbers[0]
    inUse = 0
    for num in range(len(numbers)) :
        inUse = numbers[num]
        if tmp > inUse :
            numbers[num] = tmp
            numbers[num-1] = inUse
        else :
            tmp = inUse
