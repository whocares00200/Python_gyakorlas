import math
import time

def szotar_gyak():

    jegyek ={
    
    1:{"hu":"elégtelen", "en":"insufficient"},
    2:{"hu":"elégséges", "en":"sufficient"},
    3:{"hu":"közepes", "en":"satisfactory"},
    4:{"hu":"jó", "en":"good"},
    5:{"hu":"jeles", "en":"excellent"}
            
            
    }
    

    lang = input("Válasszon nyelvet!/Select Language! (hu/en): ")
    



    if lang != "en":
        print("Enter a valid language!")

    else:
        bekérés = int(input("Kérem a jegyet: "))



        print(jegyek[bekérés][lang])




def szotar_gyak2():

    # A szótár viszont csak egyedi kulcsokat enged meg
    # A Neptun kód a kulcs, az értékek pedig az egyes hallgatók adatai egy-egy listában
    # Azonos kulcs esetén az utoljára felvett adat marad csak meg a szótárban
    h = {'ABC123':['Gipsz Jakab',{"Matek":5,'Fizika':4}],
     'XXX999':['Móricka', {"Matek":5,"Fizika":5}],
     'ABC1234':['Wincs Eszter', {"Matek":4 , "Fizika":5}]}
    


    print(h['ABC123'][0][0])



szotar_gyak2()