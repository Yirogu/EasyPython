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
    print(fizzBuzz(number))
end = time.clock()
print(start - end)
