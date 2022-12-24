a = {12:23, 2:35, 36:90, 4:64,5:11}
sorted_values = sorted(a.values())
sorted_a = {} #пустой словарь
sorted_b = {} #пустой словарь
for i in sorted_values:#для каждого элемента в отсортированном словаре
    for k in a.keys():#для ключей в словаре в
        if a[k] == i:#если ключ а равен значение
            sorted_a[k] = a[k]#сортируем 
print(sorted_a)
b = sorted(a.values(),  reverse = True)#создаем переменную с отсортированным словарем
for i in b:
    for k in a.keys():
        if a[k] == i:#если ключ равен значению
            sorted_b[k] = a[k]#даем значение
print(sorted_b)