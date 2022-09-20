from testing_sudoku import testing


# Вообщем не самый хороший вариант, но зато быстрый. Можно сделать из 1 макета ещё 3 дополнительных которые так же
# проходят тесты.
# Первые 3 знака вариантов которые создает на основе текущего макета:
# 1, 3, 9
# 2, 4, 1
# 4, 6, 3
# 7, 9, 6

number = [x for x in range(1, 10)]
sudoku_sample = [[1, 3, 9, 5, 6, 2, 4, 7, 8],
                 [2, 5, 4, 8, 9, 7, 6, 1, 3],
                 [7, 6, 8, 3, 4, 1, 9, 2, 5],
                 [5, 1, 7, 9, 2, 4, 3, 8, 6],
                 [4, 9, 6, 1, 3, 8, 7, 5, 2],
                 [3, 8, 2, 7, 5, 6, 1, 9, 4],
                 [8, 7, 5, 4, 1, 3, 2, 6, 9],
                 [9, 2, 3, 6, 7, 5, 8, 4, 1],
                 [6, 4, 1, 2, 8, 9, 5, 3, 7]
                 ]


sudoku_array = []

for i in range(1, 1000):
    rnd = i
    for x in range(0, 9):
        for y in range(0, 9):
            summ = sudoku_sample[x][y] + rnd
            if summ > 9:
                ost = summ % 9
                if ost != 0:
                    sudoku_sample[x][y] = ost
                else:
                    sudoku_sample[x][y] = 9
            else:
                sudoku_sample[x][y] = summ



test = testing(sudoku_sample)
test.testing()

#




