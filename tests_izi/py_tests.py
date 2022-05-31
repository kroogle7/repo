def ss(izi):
    '''Вычисляет является ли 
    строка полиндромом'''
    if len(izi)<=1:
        return izi
    if len(izi) > 2:
        return ss(izi[1:-1])
    return izi

print(ss('a'))
a = 5 
a += 5
print(a)

c = 1 
c+=1
print(c)