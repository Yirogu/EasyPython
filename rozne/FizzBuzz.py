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
    return text



for number in range(1,101):
    print(f"{number} result is {fizzBuzz(number)}")
end = time.clock()
first = round(end - start,9)

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
third = start3 - stop3
#the fastest solution
if first < third :
    print(f" the first is faster {third - first } ")
else :
    print(f" the third is faster {first - third} ")
print(first,third)
