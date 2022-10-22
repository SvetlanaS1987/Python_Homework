""" 1. Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ """

""" import math
from math import pi
n = pi
print(n)
d = int(input('Введи число знаков после запятой: '))
print(round(n, d))

n = float(input('Введи число: '))
d = int(input('Введи число знаков после запятой: '))
if d in [1, 10**10]:

    print("{0:.df}".format(n))

d = 3
template = '{:.' + str(d) + 'f}'
print(template.format(n))
 """
""" 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. """
""" numm = int(input('Введите натуральное число: '))
i = 2
lst = []
old = numm
while i <= numm:
      if numm % i == 0:
          lst.append(i)
          numm //= i
          i = 2
      else:
          i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}") """


""" 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. """

""" import random
list_0 = [random.randint(0,50) for i in range (15)]
print('Исходный список ', list_0)
new_list =[]
[new_list.append(i) for i in list_0 if i not in new_list ]
print('Список без повторных элементов ', new_list) """

""" 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0  """

""" import random

k = int(input('Введите коэффициент: '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))

if a != 0:
    first = (str(a) + "x^" + str(k) + " + ")
else:
    first = (str())
if b != 0:
    second = (str(b) + "x" + " + ")
else:
    second = (str())
if c != 0:
    third = (str(c) + " = 0")
else:
    third = (str())
print(f'{first}{second}{third}')
with open('m.txt', 'a') as m:
    m.write(f'{first}{second}{third}\n')
 """