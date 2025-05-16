def get_even_numbers(numbers): # Возвращает четные числа
    return [num for num in numbers if num % 2 == 0]

def find_max_and_min(numbers): # Ищет максимальное и минимальное число в неотсортированном массиве
    if not numbers:
        return None, None
    
    max_num = min_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num

        elif num < min_num:
            min_num = num
    return max_num, min_num

def quick_sort(numbers): # Реализация быстрой сортировки
    if len(numbers) <= 1:
        return numbers.copy()
    
    pivot = numbers[len(numbers) // 2]
    left = [num for num in numbers if num < pivot]
    middle = [num for num in numbers if num == pivot]
    right = [num for num in numbers if num > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def custom_sort(numbers):
    return quick_sort(numbers)

input_str = input()
numbers = [int(num.strip()) for num in input_str.split(',')]

max_num, min_num = find_max_and_min(numbers)
even_numbers = get_even_numbers(numbers)
sorted_numbers = custom_sort(numbers)

print(f"Четные числа: {even_numbers}")
print(f"Максимальное число: {max_num}")
# print(f"Максимальное число: {sorted_numbers[-1]}")
print(f"Минимальное число: {min_num}")
# print(f"Минимальное число: {sorted_numbers[0]}")
print(f"Отсортированный список: {sorted_numbers}")
