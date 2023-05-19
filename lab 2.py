#Натуральные числа, содержащие ровно К цифр. Вывести количество таких чисел. Минимальное число вывести прописью.
import re
k = 3; c = 0
clearm = []; massiv2 = []
abc = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')
f = open('labtext.txt', 'r')
massiv = f.read().split()
for l in range (len(massiv)):
    s1 = re.sub("[^0-9]", "", massiv[c])
    clearm.append(s1)
    c+=1
for i in range(len(clearm)):
    if len(clearm[i]) == k:
        massiv2.append(clearm[i])
if massiv2 == []:
    print("Таких элементов нет")
    exit()
minnum = (min(massiv2))
print(len(massiv2))
for j in str(minnum):
    for k in range(10):
        if j == str(k):
            print(abc[k])
