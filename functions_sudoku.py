import random
import copy


class func_just:

    def get_value_x_elements(sudoku, y):
        return sudoku[y]

    def get_value_y_elements(sudoku, x):
        result = []
        for control_y in sudoku:
            result.append(control_y[x])
        return result

    def view_sudoku(sudoku):

        for element in range(0, 9):
            if element + 1 % 3 == 0:
                print('\n')
                print('\n')
            print(
                f'{sudoku[element][0]["value"], sudoku[element][1]["value"], sudoku[element][2]["value"]}     {sudoku[element][3]["value"], sudoku[element][4]["value"], sudoku[element][5]["value"]}     {sudoku[element][6]["value"], sudoku[element][7]["value"], sudoku[element][8]["value"]}\n')

#     def get_value_elements_in_cube(sudoku, element_x, element_y):
#         line_1 = [0, 1, 2]
#         line_2 = [3, 4, 5]
#         line_3 = [6, 7, 8]
#
#         column_1 = [0, 1, 2]
#         column_2 = [3, 4, 5]
#         column_3 = [6, 7, 8]
#
#         control_cube = []
#
#         if element_x in line_1:
#             if element_y in column_1:
#                 for cube_x in line_1:
#                     for cube_y in column_1:
#                         control_cube.append(sudoku[cube_y][cube_x])
#
#             if element_y in column_2:
#                 for cube_x in line_1:
#                     for cube_y in column_2:
#                         control_cube.append(sudoku[cube_y][cube_x])
#
#             if element_y in column_3:
#                 for cube_x in line_1:
#                     for cube_y in column_3:
#                         control_cube.append(sudoku[cube_y][cube_x])
#
#         if element_x in line_2:
#             if element_y in column_1:
#                 for cube_x in line_2:
#                     for cube_y in column_1:
#                         control_cube.append(sudoku[cube_y][cube_x])
#
#             if element_y in column_2:
#                 for cube_x in line_2:
#                     for cube_y in column_2:
#                         control_cube.append(sudoku[cube_y][cube_x])
#
#             if element_y in column_3:
#                 for cube_x in line_2:
#                     for cube_y in column_3:
#                         control_cube.append(sudoku[cube_y][cube_x])
#
#         if element_x in line_3:
#             if element_y in column_1:
#                 for cube_x in line_3:
#                     for cube_y in column_1:
#                         control_cube.append(sudoku[cube_y][cube_x])
#
#             if element_y in column_2:
#                 for cube_x in line_3:
#                     for cube_y in column_2:
#                         control_cube.append(sudoku[cube_y][cube_x])
#
#             if element_y in column_3:
#                 for cube_x in line_3:
#                     for cube_y in column_3:
#                         control_cube.append(sudoku[cube_y][cube_x])
#
#         return control_cube


class func_hard:

    def del_duplicate_x_element(sudoku, y, element):
        for x in range(0, 9):
            sudoku[y][x]['possible_values'].remove(element)
        return sudoku

    # def count_free_x_cell(sudoku, y, element):
    #     count = 0
    #     for x in range(0, 9):
    #         if not sudoku[y][x]['status']:
    #             count +=1
    #     return count
    # def del_dublicate_x_element_dict(sudoku, y, value):
    #     for x in range(0,9):
    #         if sudoku[y][x]:
    #         sudoku[y][x]['possible_value']

    # def get_count_free_cell(sudoku, pos):
    #     for y in range(pos[0], 9):
    #         for x in range(pos[1], 9):
    #             pass



    def tested_possible_value(self,sudoku, y,x):
        old_sudoku = sudoku
        status = True
        sudoku = copy.deepcopy(old_sudoku)

        for tested_values in sudoku[y][x]['possible_values']:
            sudoku[y][x]['value'] = tested_values
            sudoku[y][x]['status'] = True
            status = True
            for y in sudoku:
                if status:
                    for x in y:
                        if not y['status']:
                            sudoku = func_hard.del_dublicate_cube(sudoku, x, y, tested_values)
                            sudoku = func_hard.del_duplicate_y_element(sudoku, x, tested_values)
                            sudoku = func_hard.del_duplicate_x_element(sudoku, y, tested_values)
                            # func_just.get_value_y_elements()
                            possible_cube = self.get_posible_cube(sudoku, y, x)
                            posible_y = self.get_possible_y(sudoku, x)
                            posible_x = self.get_possible_x(sudoku, y)

                            possible = possible_cube + posible_y + posible_x
                            possible = set(possible)
                            possible_values -= possible
                            possible_values = list(possible_values)

                            if possible_values.count() <= 0:
                                status = False
                                break
                else:
                    break

                            # count_cube = self.count_free_cell_cube()
                            # count_y_sell = self.count_free_y_cell()
                            # count_x_sell = self.count_free_x_cell()
        return sudoku




    def get_posible_cube(self,sudoku,y,x):
        result = []
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        columns = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for line in lines:
            for column in columns:
                if y in line:
                    if x in column:
                        for cube_y in line:
                            for cube_x in column:
                                result.append(sudoku[cube_y][cube_x]['posible_values'])
        return result


    def get_possible_x(self,sudoku, y):
        result = []
        for y in sudoku:
            for x in y:
                result.append(x['possible_values'])
        return result

    def get_possible_y(self,sudoku, x):
        result = []
        for control_y in sudoku:
            result.append(control_y[x]['posible_values'])
        return result



    def del_duplicate_y_element(sudoku, x, element):
        for y in range(0, 9):
            sudoku[y][x]['possible_values'].remove(element)
        return sudoku

    def count_free_y_cell(sudoku, x, element):
        count = 0
        for y in range(0, 9):
            if not sudoku[y][x]['status']:
                count+=1
        return count

    # def check_possible_value(self, sudoku, pos):
    #     for y in range(pos[0], 9):
    #         for x in range(pos[1], 9):
    #             pos = [y,x]
    #             self.get_count_free_cell(sudoku, pos)
    #             pass


    # def count_possible_value_x(sudoku,y):
        # for x in range(0, 9):
            # sudoku[y][x]['possible_values']
        # return sudoku


    def del_dublicate_cube(sudoku, x, y, element):

        lines = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
        columns = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]

        for line in lines:
            for column in columns:
                if y in line:
                    if x in column:
                        for cube_y in line:
                            for cube_x in column:
                                try:
                                    sudoku[cube_y][cube_x]['possible_values'].remove(element)
                                except:
                                    pass

        return sudoku

    # def count_free_cell_cube(sudoku, x, y):
    #
    #     lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    #     columns = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    #     count = 0
    #     for line in lines:
    #         for column in columns:
    #             if y in line:
    #                 if x in column:
    #                     for cube_y in line:
    #                         for cube_x in column:
    #                             if not sudoku[cube_y][cube_x]['status']:
    #                                 count+=1
    #
    #     return count
    #
    # def get_started_cube_values(sudoku):
    #     set_started_cube = [[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
    #                         [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
    #                         [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]]
    #
    #     for cube in set_started_cube:
    #         possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #         for pos in cube:
    #             random_value = random.choice(possible_values)
    #             possible_values.remove(random_value)
    #             sudoku[pos[0]][pos[1]] = random_value
    #
    #     return sudoku

    def get_started_cube_values_dict(sudoku):
        set_started_cube = [[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
                            [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
                            [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]]

        for cube in set_started_cube:
            possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for pos in cube:
                random_value = random.choice(possible_values)
                possible_values.remove(random_value)
                sudoku[pos[0]][pos[1]] = {'status': True, 'possible_values': False, 'value': random_value}
        return sudoku


    def get_started_field():
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        sudoku = [[[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], []]]

        for row in range(0, 9):
            for column in range(0, 9):
                sudoku[row][column] = {'status': False, 'possible_values':numbers, 'value': 0}


    # def check_count_posible_element(sudoku, position, value):
    #     pass


    # def get_started_field_dict(self):
    #     sudoku = []
    #
    #     for row in range(0, 9):
    #         sudoku[row] = {'status' : True,}