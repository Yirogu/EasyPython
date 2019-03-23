from random import randint
def Pytania (ilosc_pytan,pyta = []) :
    for x in range(0,ilosc_pytan) :
        pyta.append(randint(1,1000))
    return pyta
ilosc_pytan = int(input("ile pytan ma zawierac egzamin : "))
print(Pytania(ilosc_pytan))
