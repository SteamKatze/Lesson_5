import random

# Створюємо список з 10 випадкових цілих чисел
numbers = [random.randint(-100, 100) for _ in range(10)]

# Виводимо список для перевірки
print("Початковий список цілих чисел:", numbers)

# Створюємо списки цілих чисел згідно з вимогами
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]
negative_numbers = [x for x in numbers if x < 0]
positive_numbers = [x for x in numbers if x > 0]

# Виводимо результати
print("Список парних чисел:", even_numbers)
print("Список непарних чисел:", odd_numbers)
print("Список негативних чисел:", negative_numbers)
print("Список позитивних чисел:", positive_numbers)
