import math
import time

#2023.09.30 - Szombat

#lista,tuple és dictionary gyakorlása 

def lista_gyak():
    
    lista = ["piros","kék","zöld"] #lista megadása


    print(lista)
    print(len(lista))    #lista hosszúsága


    print(lista[1])   #lista n-edik elemének megadása (az elemek 0-tól kezdődnek!!!!!!) 

    lista.append("Lófasz")    #listához elem hozzáadása

    print(lista)       


    lista.remove("Lófasz")   #listából elem eltávolítása


    print(lista)



def tuple_gyak():


    kek = (1,2,3,4,5,6,7,8,9,10,"Lófasz")

    print(kek)


    print(kek[3])

    igazvagynem = 3 in kek   #megénzi, hogy a 3-as benne van-e a tuple-ban, majd ad egy boolean értéket 

    print(igazvagynem)

    print(type(igazvagynem))

    print(kek.index(10))

    

    if 10 in kek:
        print("10 benne van a kek tuple-ban ")



def dictionary_gyak():

    szotar = {
        "manufacturer" : "Lockheed Martin",
        "year" : 1971
    }

    print(szotar)

    print(szotar["year"])

    for x in szotar:    #kiprinteli a kulcsokat, de az értékeket nem
        print(x)


    szotar["year"] = 1999  #érték felülírása a kulcs megadásával, majd egyenlőségjellel.
    print(szotar["year"])

dictionary_gyak()


    




    



