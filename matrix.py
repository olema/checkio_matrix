#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задача с сайта checkio.org
Подсчитать количество соседей клетки (на одну клетку
верх, низ, лево, право, диагонали)
в матрице.
'''


# Функция подсчета
def counter(matrix, row, col):
    '''Функция подсчитывает количество соседов у клетки с координатами
    row, col в матрице кортежей matrix -> кол-во соседей
    '''
    # Список с правильными координатами для подсчета
    valid_coords = []
    near_cell = 0
    # Ширина и высота переданной матрицы
    if matrix:
        rows = len(matrix)
        cols = len(matrix[0])
        print(rows, cols, row, col)
        print((0 <= row <= row-1))
        # Проверяем вхождение переданных координат в диапазон
        if (0 <= row <= rows-1) and (0 <= col <= cols-1):
            # Получаем список координат вокруг точки
            coords = [[r, c] for r in range(row-1, row+2) for c in range(col-1, col+2)]
            print(coords)
            # Убираем координаты, выходящие за края
            # и координаты самой точки
            for i in coords:
                print(i)
                if (0 <= i[0] < rows) and (0 <= i[1] < cols):
                    if not ((i[0] == row) and (i[1] == col)):
                        valid_coords.append(i)
            # Считаем количество соседей
            for r,c in valid_coords:
                print(r,c)
                near_cell += matrix[r][c]
        print(valid_coords)
    return near_cell

def main():
    m = ((1, 0, 0, 1),
         (0, 1, 1, 0),
         (1, 0, 0, 1),
         (0, 0, 0, 1),)
    r = 3
    c = 3
    print('*' * 20)
    print(r,c)
    for i in m:
        print(i)
    print(counter(m, r, c))



if __name__ == '__main__':
    main()


