import random

# Створюємо список з 10 випадкових цілих чисел
numbers = [random.randint(-100, 100) for _ in range(10)]

# Виводимо список для перевірки
print("Список цілих чисел:", numbers)

# Знаходимо індекси мінімального та максимального значень
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

# Міняємо місцями мінімальне та максимальне значення
numbers[min_index], numbers[max_index] = max(numbers), min(numbers)

# Обчислюємо суму негативних чисел
sum_negative = sum(x for x in numbers if x < 0)

# Обчислюємо суму парних чисел
sum_even = sum(x for x in numbers if x % 2 == 0)

# Обчислюємо суму непарних чисел
sum_odd = sum(x for x in numbers if x % 2 != 0)

# Обчислюємо добуток елементів з кратними індексами 3
product_index3 = 1
for i in range(len(numbers)):
    if i % 3 == 0:
        product_index3 *= numbers[i]

# Знаходимо перший і останній позитивні індекси
positive_indices = [i for i, x in enumerate(numbers) if x > 0]
if positive_indices:
    first_positive_index = positive_indices[0]
    last_positive_index = positive_indices[-1]

    # Обчислюємо суму елементів, що знаходяться між першим та останнім позитивними елементами
    sum_between_positives = sum(numbers[first_positive_index + 1:last_positive_index])
else:
    sum_between_positives = 0

# Виводимо результати
print("Сума негативних чисел:", sum_negative)
print("Сума парних чисел:", sum_even)
print("Сума непарних чисел:", sum_odd)
print("Добуток елементів з кратними індексами 3:", product_index3)
print("Добуток елементів між мінімальним та максимальним елементом:", min(numbers) * max(numbers))
print("Сума елементів, що знаходяться між першим та останнім позитивними елементами:", sum_between_positives)