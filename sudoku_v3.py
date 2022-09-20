import random
from testing_sudoku import testing
from functions_sudoku import func_hard, func_just
import copy


sudoku = func_hard.get_started_field()

sudoku = func_hard.get_started_cube_values_dict(sudoku)


result_sudoku =[]
for y in sudoku:
    for x in y:
        if not y['status']:
            result_sudoku = func_hard.tested_possible_value(sudoku, y,x)


func_just.view_sudoku(result_sudoku)

            # if func_hard.test_possible_values():
            #     sudoku = tested_sudoku
            # else:
            #     tested_values = y['possible_value'][0] + 1






