class testing:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def testing(self):
        if self.__cube_testing():
            print('cube_test: Faild')
            return False
        elif self.__axis_y_test():
            print('first_test: Faild')
            return False
        elif self.__axis_x_test():
            print('twice_test: Faild')
            return False
        else:
            print('testing was successful')
            return True


    def __axis_y_test(self):
        for x in self.sudoku:
            if len(set(x)) == len(x):
                return False

    def __axis_x_test(self):
        for x in range(0, 9):
            for y in range(0, 9):
                test_sample = []
                test_sample.append(self.sudoku[y][x])
                if len(set(test_sample)) != 9:
                    return False

    def __cube_testing(self):
        range_tested = [[0, 3], [3, 6], [6, 9]]

        for x in range_tested:  # 0-3
            for q in range(x[0], x[1]):  # 0-3 3-6 6-9

                for w in range_tested:  # 0-3
                    for e in range(w[0], w[1]):  # 0-3 3-6 6-9
                        test_sample = []
                        test_sample.append(self.sudoku[q][e])
                        if len(set(test_sample)) != 9:
                            return False

        return True
#
# 00 01 02    03 04 05    06 07 08
# 10 11 12    13 14 15    16 17 18
# 20 21 22    23 24 25    26 27 28

# 30 31 32    33 34 35    36 37 38
# 40 41 42    43 44 45    46 47 48
# 50 51 52    53 54 55    56 57 58
#
# 60 61 62    63 64 65    66 67 68
# 70 71 72    73 74 75    76 77 78
# 80 81 82    83 84 85    86 87 88

# sudoku_ =        [[1, 3, 9,    5, 6, 2,    4, 7, 8],
#                  [2, 5, 4,    8, 9, 7,    6, 1, 3],
#                  [7, 6, 8,    3, 4, 1,    9, 2, 5],
#
#                  [5, 1, 7,    9, 2, 4,    3, 8, 6],
#                  [4, 9, 6,    1, 3, 8,    7, 5, 2],
#                  [3, 8, 2,    7, 5, 6,    1, 9, 4],
#
#                  [8, 7, 5,    4, 1, 3,    2, 6, 9],
#                  [9, 2, 3,    6, 7, 5,    8, 4, 1],
#                  [6, 4, 1,    2, 8, 9,    5, 3, 7]
#                  ]

# sud = set([set([1,2]),set([1,2])])
# print(sud)