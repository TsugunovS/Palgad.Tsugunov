from math import * 
from random import *
from module1 import * 
#21/02/23
#Практическая работа "Palgad"
#9. Top() - Т самых бедных и самых богатых человека
palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

while True:
    nimi = input("Sisestage nimi (väljumiseks sisestage 'väljund'): ")
    if nimi == 'väljund':
        break
    inimesed.append(nimi)
    palg = int(input("Sisestage palgad: "))
    palgad.append(palg)





