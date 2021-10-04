from os import sep
import pandas as pd
x = [[0]*8, [0]*8, [0]*8]
file = open("Data.txt")
j = 0; k = 0; buf = ''
#Считывание из файла
for line in file:
    values  = list(map(float, line.split()))
    x[0][k] = values[0]
    x[1][k] = values[1]
    x[2][k] = values[2]
    k += 1
#Считывание из файла завершено
DF = pd.DataFrame(x).transpose()
M = DF.mean()   # Мат ожидание
SD = DF.std()   # Дисперсия
covMatrix = DF.cov()    # Ковариационная матрица
corrMatrix = DF.corr()  # Корреляционная матрица


# Вывод данных
print("Исходные данные\n", DF, sep='')
print("Математические ожидания\n", M, sep='')
print("Дисперсии\n", SD, sep='')
print("Ковариационная матрица\n", covMatrix, sep='')
print("Корреляционная матрица\n", corrMatrix, sep='')
