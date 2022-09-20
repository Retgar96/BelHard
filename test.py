from functions_sudoku import func_just,func_hard

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sudoku = [[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]]

for row in range(0, 9):
    for column in range(0, 9):
        sudoku[row][column] = numbers




for y in range(0, 9):
    for x in range(0, 9):
        item = int(input(f'Введите значение для поля{y, x}\n'))


        sudoku = func_hard.del_dublicate_cube(sudoku, y, x, item)
        sudoku[y][x] = [item]

        func_just.view_sudoku(sudoku)
        # for row_ in range(0, 9):
        #     for column_ in range(0, 9):
        #         if row != row_:
        #             if column != column_:
        #                 sudoku[row_]

                # item = sudoku[row_][column_]
                # res = set(sudoku[row][column])
