def Top(palgad, inimesed, T):
    n = len(palgad)
    if T >= n:
        return inimesed
    else:
        # Sorteerimine
        # Сортируем
        sort_index = sorted(range(n), key=lambda i: palgad[i])
        # Saame T vaeseima ja T rikkaima nimekirja
        # Получаем список из T самых бедных и T самых богатых
        top = inimesed[sort_index[:T]] + inimesed[sort_index[-T:]]
        return top

    

