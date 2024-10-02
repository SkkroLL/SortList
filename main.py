import random
import time

#заполнение массива
list_numbers = []
input_range = int(input("Введите количество элементов в массиве: "))
a = 0
while a != input_range:
    list_numbers.append(random.randint(1, 10))
    a += 1
print(f'Ваш список: {list_numbers}')

#Методы сортировки
def bubble_sort(arr):
  n = len(arr)
  swaps = 0
  for i in range(n - 1):
    for j in range(n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swaps += 1
  return arr, swaps
def selection_sort(arr):
  n = len(arr)
  swaps = 0
  for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
      if arr[min_idx] > arr[j]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    swaps += 1
  return arr, swaps
def insertion_sort(arr):
  n = len(arr)
  swaps = 0
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
      swaps += 1
    arr[j + 1] = key
  return arr, swaps
def quick_sort(arr):
  if len(arr) <= 1:
    return arr, 0
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    less, swaps_less = quick_sort(less)
    greater, swaps_greater = quick_sort(greater)
    return less + [pivot] + greater, swaps_less + swaps_greater + len(greater)
def shaker_sort(arr):
  n = len(arr)
  swapped = True
  start = 0
  end = n - 1
  swaps = 0
  while swapped:
    swapped = False
    for i in range(start, end):
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swaps += 1
        swapped = True
    end -= 1
    if swapped:
      swapped = False
      for i in range(end - 1, start - 1, -1):
        if arr[i] > arr[i + 1]:
          arr[i], arr[i + 1] = arr[i + 1], arr[i]
          swaps += 1
          swapped = True
      start += 1
  return arr, swaps

#таймер
start_time = time.time()

#выбор сортировки
choice_input = int(input('\nВыберите метод сортировки: \n1. bubble_sort\n2. selection_sort\n3. insertion_sort\n4. quick_sort\n5. shaker_sort\nВведите цифру сортировки: '))
if choice_input == 1:
    sort_list, swaps = bubble_sort(list_numbers)
    print(f'Отсортированный список: {sort_list}')
    print(f'количество перестановок: {swaps}')
elif choice_input == 2:
    sort_list, swaps = selection_sort(list_numbers)
    print(f'Отсортированный список: {sort_list}')
    print(f'количество перестановок: {swaps}')
elif choice_input == 3:
    sort_list, swaps = insertion_sort(list_numbers)
    print(f'Отсортированный список: {sort_list}')
    print(f'количество перестановок: {swaps}')
elif choice_input == 4:
    sort_list, swaps = quick_sort(list_numbers)
    print(f'Отсортированный список: {sort_list}')
    print(f'количество перестановок: {swaps}')
elif choice_input == 5:
    sort_list, swaps = shaker_sort(list_numbers)
    print(f'Отсортированный список: {sort_list}')
    print(f'количество перестановок: {swaps}')
else:
    print('Ошибка!')

end_time = time.time()
print(f'Время сортировки: {round(end_time - start_time, 2)}')