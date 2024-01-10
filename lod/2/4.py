numbers = []

sum_num = 0
max_num = float('-inf')
min_num = float('inf')

# Обработка ввода чисел
while True:
    try:
        number = int(input("Введите число (или 7 для выхода): "))
        if number == 7:
            break
        numbers.append(number)
        sum_num += number
        max_num = max(max_num, number)
        min_num = min(min_num, number)
    except ValueError:
        print("Введенное значение не является числом. Попробуйте еще раз.")

# Вывод результатов
if numbers:
    print("Сумма введенных чисел: ", sum_num)
    print("Максимальное число: ", max_num)
    print("Минимальное число: ", min_num)
else:
    print("Введено недопустимое значение.")

print("Good bye!")