import random
from testing_sudoku import testing
from functions_sudoku import func_just,func_hard


sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]







sudoku = func_hard.get_started_cube_values(sudoku)

# Получаем позицию курсора
for element_y in range(0, 9):
    for element_x in range(0, 9):
        if sudoku[element_y][element_x] == 0:
            # Создаем set значений что бы после слияния получить только возможные значения
            possible_values = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            control = []

            # Получаем все значения из строки на которой находится курсор
            control += func_just.get_value_x_elements(sudoku, element_y)

            # Получаем все значения из столбцов которые на линии курсора
            control += func_just.get_value_y_elements(sudoku, element_x)

            # Получаем все значения из квадратов
            control += func_just.get_value_elements_in_cube(sudoku, element_x, element_y)

            # Удаляем дубликаты
            control = set(control)

            # Получаем значения которые свободны для данной ячейки
            possible_values = possible_values - control
            possible_values = list(possible_values)
            if not possible_values:
                print(element_y, element_x, 'Хуйня сабачья')

            # Выбираем рандомный элемент из получившегося массива
            try:
                rnd = random.choice(possible_values)
                sudoku[element_y][element_x] = rnd
            except:
                print(f'elemement {element_y, element_x} шлет тебя нахуй')
            # view_sudoku(sudoku)
            # print('')
            # 3,4,6






func_just.view_sudoku(sudoku)
test = testing(sudoku)
test.testing()
print(sudoku)