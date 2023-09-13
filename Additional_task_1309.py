import random

# Створюємо матрицю 10x10 і заповнюємо її випадковими числами від 10 до 99
matrix = []
for _ in range(10):
    row = []
    for _ in range(10):
        row.append(random.randint(10, 99))
    matrix.append(row)

# Виводимо матрицю
for row in matrix:
    for number in row:
        print(number, end=" ")
    print()

# Виводимо суму чисел головної діагоналі
main_diagonal_sum = sum(matrix[i][i] for i in range(10))
print("Сума чисел головної діагоналі:", main_diagonal_sum)

# Знаходимо мінімальне та максимальне значення побічної діагоналі
secondary_diagonal_values = [matrix[i][9 - i] for i in range(10)]
min_secondary_diagonal = min(secondary_diagonal_values)
max_secondary_diagonal = max(secondary_diagonal_values)
print("Мінімальне значення побічної діагоналі:", min_secondary_diagonal)
print("Максимальне значення побічної діагоналі:", max_secondary_diagonal)

# Введення номеру стовпця та виведення чисел з цього стовпця
column_number = int(input("Введіть номер стовпця (0-9): "))
column_values = [matrix[i][column_number] for i in range(10)]
print("Числа зі стовпця {}:".format(column_number))
print(column_values)

# Введення двох номерів стовпців та обмін їх місцями
swap_column1 = int(input("Введіть номер першого стовпця для обміну (0-9): "))
swap_column2 = int(input("Введіть номер другого стовпця для обміну (0-9): "))

# Перевірка правильності введених номерів стовпців
if 0 <= swap_column1 < 10 and 0 <= swap_column2 < 10:
    # Обмін стовпців
    for i in range(10):
        matrix[i][swap_column1], matrix[i][swap_column2] = matrix[i][swap_column2], matrix[i][swap_column1]

    # Виведення матриці після обміну
    print("Матриця після обміну стовпців {} і {}: ".format(swap_column1, swap_column2))
    for row in matrix:
        for number in row:
            print(number, end=" ")
        print()
else:
    print("Неправильно введені номери стовпців.")