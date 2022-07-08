# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


def get_coord(mes):
    x = float(input(f'{mes}, x: '))
    y = float(input(f'{mes}, y: '))
    coord = [x, y]
    return coord


def distance(A=[], B=[]):
    p1 = (A[0]-B[0])**2
    p2 = (A[1]-B[1])**2
    res = round(math.sqrt(p1 + p2), 2)
    print(res)


a = get_coord('Введите координату первой точки ')
b = get_coord('Введите координату второй точки ')

distance(a, b)