from math import * 
from random import *
from module1 import * 
#21/02/23
#Практическая работа "Palgad"
#9. Top() - Т самых бедных и самых богатых человека

#3
palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]
#leiab palgad nimekirjast maksimumpalga
#находит максимальную зарплату в списке palgad
max_palga_indeks = palgad.index(max(palgad))
max_palga_saanu = inimesed[max_palga_indeks]
#näitab maksimumpalka
#показывает максимальную зарплату
print(f" Kõrgeim palk ({max(palgad)}) saab {max_palga_saanu}.")



#9
palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

# liita loendid loendiks
# объединить списки в список
andmed = list(zip(palgad, inimesed))

# sorteerige loend kasvavas järjekorras
# сортируем список по возрастанию зарплаты
andmed.sort()

# väljund T vaesemad inimesed
# выводим T самых бедных человек
T = 2
print(f"T Kõige vaesemad inimesed: {andmed[:T]}")

# sorteerige loend kahanevas järjekorras
# сортируем список по убыванию
andmed.sort(reverse=True)

# väljund T rikkaimad inimesed
# выводим T самых богатых человек
print(f"T Kõige rikkaim inimesed: {andmed[:T]}")






