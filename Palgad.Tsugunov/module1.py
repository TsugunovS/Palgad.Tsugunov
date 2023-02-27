def Vordsed_palgad(i:list,p:list):
    dublikatid=[x for x in p if p.count(x)>1]
    dublikatid=list(set(dublikatid)) # [1200, 2500, 750, 395, 1200]->[1200,750]
    for palk in dublikatid:
        n=p.count(palk) #1200, n=2; 750, n=2
        k=-1 #----
        print(f"{palk} saavad kätte järgmised inimesed:")
        for j in range (n):
            k=p.index(palk,k+1)#----
            nimi=i[k]
            print(nimi)




def Sorteerimine(i:list,p:list):
    v=int(input("palk 1-kahaneb,2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0, n-1):
            for k in range (j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
        else:
            n=len(p)
            for j in range(0, n-1):
                for k in range (j+1,n):
                    if p[j]>p[k]:
                        abi=p[j]
                        p[j]=p[k]
                        p[k]=abi
                        abi=i[j]
                        i[j]=i[k]
                        i[k]=abi




def Kustutamine(i:list, p:list):
    """
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi: ")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=j.index(nimi)
            i.pop(ind)
            p.pop(ind)



#9 Top() - Т самых бедных и самых богатых человека
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def Rikasvaene(palgad, inimesed, t):
    andmed = list(zip(palgad, inimesed))
    andmed.sort()
    vaesemad = andmed[:t]
    print(f"T Kõige vaesemad inimesed: {vaesemad}")
    andmed.sort(reverse=True)
    rikkaimad = andmed[:t]
    print(f"T Kõige rikkaimad inimesed: {rikkaimad}")



#3 Самую большую зарплату и кто ее получает
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def Kõrgeimpalk(palgad, inimesed):
    # находим индекс максимальной зарплаты
    max_palga_indeks = palgad.index(max(palgad))
    # находим имя человека
    max_palga_saanu = inimesed[max_palga_indeks]
    print(f" Kõrgeim palk ({max(palgad)}) saab {max_palga_saanu}.")

    

