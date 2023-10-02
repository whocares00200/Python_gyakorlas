import math
import numpy
#Térfogat és felszín számítása egy téglatestnek

def teglatest():
    a = int(input("A oldal: "))
    b = int(input("B oldal: "))
    c = int(input("C oldal: "))

    felszin =2*((a*b)+(b*c)+(a*c)) 
    
    terfogat = a*b*c

    print(f'A felszín: {felszin}')
    print(f'A térfogat: {terfogat}')







def melyiknagyobb():
    a = int(input("Kérem az egyik számot: "))
    b = int(input("Kérem az másik számot: "))

    t = (a, b)

    t_sorted = (sorted(t))

    print("A számok sorban: ")

    for x in t_sorted:
        print(x)

#Ezek a functionok megadják az inputok közül a legkisebb számot

def legkisebb():                                        #legegyszerűbb megoldás
    a = int(input("Kérem az egyik számot: "))

    b = int(input("Kérem az másik számot: "))

    minimal = min(a,b)

    print(f'A kisebbik szám: {minimal}')




def legkisebb2():                                       #komplikáltabb, de szintén jó megoldás
    a = int(input("Kérem az egyik számot: "))

    b = int(input("Kérem az másik számot: "))

    if a >= b:
        print(f'A kisebbik szám: {b}')

    elif b >= a:
        print(f'A kisebbik szám: {a}')

#While ciklus gyakorlasa

def while_ciklus_teszt():                             #amíg a while ciklus feltétele True, addig futtatja a megadott parancsot, False feltétel esetén, pedig kilép

    #age = int(input("Hány éves vagy? "))             #Ez így nem jó, mivel a True esetén infinite loopot csinálna a while-ból

    age_limit = 18

    while int(input("Hány éves vagy? ")) < age_limit:
        print(f'Sajnálom, legalább {age_limit} évesnek kell lenned!')


    print("Tessék, itt a sör!")




def szobafestés():

    a = float(input("Szoba a oldalának hossza: "))
    b = float(input("Szoba b oldalának hossza: "))
    c = float(input("Szoba c oldalának hossza: "))
    
    natur_felszin =2*((a*b)+(b*c)+(a*c))

    d = float(input("Ablak egyik oldalának hossza: "))
    e = float(input("Ablak másik oldalának hossza: "))

    ablak_felszin = e*d

    festendo_felszin = natur_felszin - ablak_felszin

    festek_efficiency = 0.5

    szukseges_festek = festendo_felszin / festek_efficiency

    print(f'A szoba lefestéséhez {szukseges_festek} L festék szükséges. ')





def while_loop():    #limit-ig írja ki a számokat
    
    limit = int(input("Set the loop limit: "))
    
    a = 1
    while a<limit:
        print(a, end = " ")
        a = a+1



while_loop()