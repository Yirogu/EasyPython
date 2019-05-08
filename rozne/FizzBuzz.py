# Wypisz wszystkie liczby od 1 do 100
# Jeśli liczba jest podzielna przez trzy wypisz “Fizz“
# Jeśli liczba jest podzielna przez pięć wypisz “Buzz“
# Jeśli liczba jest podzielna przez trzy i pięć wypisz “FizzBuzz“
import time


# First Idea
start = time.clock()
def fizzBuzz(number):
    text = ""
    if number % 3 == 0 :
        text = "Fizz"
    if number % 5 == 0 :
        text += "Buzz"
    if text == "":
        text = number
    print(text)



for number in range(1,101):
    fizzBuzz(number)
end = time.clock()
first = end - start

#Time  to execute : 0.00030799999999999925,0.0003490000000000021,0.0004289999999999988

#Second Idea without use def



start2 = time.clock()
for number in range(1,101):
    text = ""
    if number % 3 == 0 :
        text = "Fizz"
    if number % 5 == 0 :
        text += "Buzz"
    print(f"{number} result is {text}")
end2 = time.clock()
second = end2 - start2
second = round(second,9)

#Simple resolution from internet
start3 = time.clock()
for num in range(1, 101):
    string = ""
    if num % 3 == 0:
        string = "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if string == "":
        string = str(num)
    print(string)
stop3 = time.clock()
third = stop3 -start3

# fourth Idea
start4 = time.clock()
def fizzBuzz(number):
    text = ""
    if number % 15 == 0 :
        return "FizzBuzz"
    if number % 3 == 0 :
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    else :
        return number




for number in range(1,101):
    print(fizzBuzz(number))
end4 = time.clock()
fourth = end4 - start4

# fifth Idea
start5 = time.clock()

def fizzBuzz(number):
    if number % 15 == 0 :
        return "FizzBuzz"
    if number % 3 == 0 :
        return "Fizz"
    else:
        return "Buzz"

def indivisible(number):
    if number % 3 != 0 and number % 5 != 0 :
        return number
    else:
        return fizzBuzz(number)






for number in range(1,101):
    print(indivisible(number))
end5 = time.clock()
fifth = end5 - start5

# six Idea
start6 = time.clock()

def fizzBuzz(number):
    text = ""
    if number % 3 == 0 :
        text = "Fizz"
    if number % 5 == 0 :
        text += "Buzz"
    return text

def indivisible(number):
    if number % 3 != 0 and number % 5 != 0 :
        return number
    else:
        return fizzBuzz(number)






for number in range(1,101):
    print(indivisible(number))
end6 = time.clock()
six = end6 - start6

# seventh Idea
start7 = time.clock()

def fizzBuzz(number):
    text = ""
    if number % 3 == 0 :
        text = "Fizz"
    if number % 5 == 0 :
        text += "Buzz"
    print(text)

def indivisible(number):
    if number % 3 != 0 and number % 5 != 0 :
        print(number)
    else:
        fizzBuzz(number)







for number in range(1,101):
    indivisible(number)
end7 = time.clock()
seventh = end7 - start7


#the fastest solution
if third < six :
    print(f" the third is faster {six - third } ")
else :
    print(f" the six is faster {third - six} ")
print(six,seventh)
