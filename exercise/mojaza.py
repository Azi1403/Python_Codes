def separator(ls):
    zojha = []
    fardha = []
    for num in ls:
        if num%2==0:
            zojha.append(num)
        else:
            fardha.append(num)

    print((sorted(zojha),sorted(fardha)))

separator([-3, -2, -1, 0, 1, 2, 3]) # in question ask us show it in tople so we input numbers between ()