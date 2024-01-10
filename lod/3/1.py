diapazonn = int(input("Введите начало диапазона для поиска простых чисел: "))
diapazonk = int(input("Введите конец диапазона для поиска простых чисел: "))
for num in range(diapazonn, diapazonk):
    count = 0
    delitel = 2
    while delitel < num:
        if num % delitel == 0:
            count += 1
        delitel += 1
    if count == 0:
        print(f'{num} простое число')