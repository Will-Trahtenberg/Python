karta = list(map(int,input().split()))
slovar = {}
karta1 = set(karta)
print(karta1)
for i in karta1:
    slovar[i] = karta.count(i)
    print(i, karta.count(i))
s1 = sorted(slovar.values())
s2 = sorted(slovar.keys())
if s1 == [1, 4]:
    print('Каре')
elif s1 == [2, 3]:
    print('Фулл хауз')
elif s1 == [1, 1, 1, 1, 1]:
    if s2[1] - s2[0] == 1 and s2[2] - s2[1] == 1 and s2[3] - s2[2] == 1 and s2[4] - s2[3] == 1:
        print('стрит')
    else:
        print('старшая карта')
elif s1 == [1, 1, 3]:
    print('Сет')
elif s1 == [1, 2, 2]:
    print('Две пары')
elif s1 == [1, 1, 1, 2]:
    print('Пара')
elif s1 == [5]:
    print('шулер')