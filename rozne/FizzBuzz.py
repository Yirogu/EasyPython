# Wypisz wszystkie liczby od 1 do 100
# Jeśli liczba jest podzielna przez trzy wypisz “Fizz“
# Jeśli liczba jest podzielna przez pięć wypisz “Buzz“
# Jeśli liczba jest podzielna przez trzy i pięć wypisz “FizzBuzz“
import time

# First Idea
def fizzBuzz(number):
    text = ""
    if number % 3 == 0 :
        text = "Fizz"
    if number % 5 == 0 :
        text += "Buzz"
    return text


start = time.clock()
for number in range(1,100):
    print(f"{number} result is {fizzBuzz(number)}")
end = time.clock()
first = end - start
#Time  to execute : 0.00030799999999999925,0.0003490000000000021,0.0004289999999999988

#Second Idea without use def



start2 = time.clock()
for number in range(1,100):
    text = ""
    if number % 3 == 0 :
        text = "Fizz"
    if number % 5 == 0 :
        text += "Buzz"
    print(f"{number} result is {text}")
end2 = time.clock()
second = end2 - start2

#the fastest solution
if first > second :
    print(f" the first is faster {first - second} ")
else :
    print(f" the second is faster {second - first} ")
print(first,second)
