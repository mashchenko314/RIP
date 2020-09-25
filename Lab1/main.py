from math import sqrt
import sys

if len(sys.argv) == 4:
    try:
        print('Мащенко Елена ИУ5-55Б')
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except:
        print('Введены некорректные аргументы')
        exit()
else:
    print('Мащенко Елена ИУ5-55Б')
    if  len(sys.argv) == 2:
        a = float(sys.argv[1])
        b = float(input('Введите b: '))
        c = float(input('Введите c: '))
    elif len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(input('Введите c: '))
    else :
        a = float(input('Введите a: '))
        b = float(input('Введите b: '))
        c = float(input('Введите c: '))

if a==0 and b==0 and c==0:
    print("Бесконечное множество решений")
    exit()
elif a != 0:
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print('Уравнение не имеет решений')
        exit()
    else:
        x1 = (-b + sqrt(discriminant) / (2 * a))
        x2 = (-b - sqrt(discriminant) / (2 * a))
        if x1 >= 0 or x2 >= 0:
            print('Уравнение имеет решение')
        else:
            print('Уравнение не имеет решений')
            exit()

    if x1 >= 0:
        x11 = sqrt(x1)
        x12 = -sqrt(x1)
        print(x11 ,x12)
    if x2 >= 0:
        x21 = sqrt(x2)
        x22 = -sqrt(x2)
        print(x21, x22)
else:
    try:
        x1 = sqrt(-c/b)
        x2 = -sqrt(-c/b)
        print(x1 ,x2)
    except:
        print("Уравнение не имеет решений")