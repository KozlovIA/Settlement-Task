import statistics as stat
x = [[0]*8, [0]*8, [0]*8]
file = open("Data.txt")
j = 0; k = 0; buf = ''
#Считывание из файла
for line in file:
    for i in range(len(line)):
        if line[i] == ' ' or line[i] == '\n':
            x[j][k] = buf; j += 1
            buf = ''
            continue
        else:
            buf += line[i]
    j = 0; k += 1
#Считывание из файла завершено
m = stat.mean(x[1])
print(m)
