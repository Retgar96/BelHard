number = [1, 2, 3, 4, 5]


for i in range(len(number)):

    if i == len(number):
        j = 0
    if i == 0:
        j = len(number)
    j = i-1
    r = i+1
    print(number[i]+number[j]+number[r])