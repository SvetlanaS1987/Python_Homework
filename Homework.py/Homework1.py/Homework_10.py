""" 1. Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания. """


""" a = [1, 2, 3]
b = [4, 3, 2]

w = set(a)
q = set(b)
c = w.intersection(q)
d = sorted(list(c))
print(*d, sep=' ') """


""" 2.Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), 
если это число ранее встречалось в последовательности или NO, если не встречалось """

""" a = [int(s) for s in input().split(' ')]
num = set()
for i in a:
    if i not in num:
        print('NO')
        num.add(i)
    else: 
        print('YES') """


""" 3.Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
Sample Input:
4
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.
Sample Output:
19 """

""" count = int(input('Введи количество строк: '))
some_list = []
for i in range(count):
    for el in input().split():
        some_list.append(el)
print(len(set(some_list))) """
