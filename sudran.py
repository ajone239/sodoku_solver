'''
Jo's solution
'''
import time
import numpy as np
from numpy import random

# Setting up un-solved puzzle
# '''
puz = np.array(
    [[0, 7, 0, 0, 5, 0, 0, 0, 0],
     [0, 5, 1, 6, 0, 9, 2, 0, 0],
     [4, 0, 6, 2, 0, 7, 0, 0, 1],
     [0, 8, 7, 0, 0, 0, 1, 0, 0],
     [3, 0, 0, 8, 0, 4, 0, 0, 2],
     [0, 0, 4, 0, 0, 0, 5, 9, 0],
     [1, 0, 0, 7, 0, 5, 8, 0, 9],
     [0, 0, 8, 3, 0, 2, 4, 7, 0],
     [0, 0, 0, 0, 4, 0, 0, 1, 0]])
'''
puz = np.array(
    [[0, 2, 0, 4, 5, 6, 7, 8, 9],
     [4, 5, 7, 0, 8, 0, 2, 3, 6],
     [6, 8, 9, 2, 3, 7, 0, 4, 0],
     [0, 0, 5, 3, 6, 2, 9, 7, 4],
     [2, 7, 4, 0, 9, 0, 6, 5, 3],
     [3, 9, 6, 5, 7, 4, 8, 0, 0],
     [0, 4, 0, 6, 1, 8, 3, 9, 7],
     [7, 6, 1, 0, 4, 0, 5, 2, 8],
     [9, 3, 8, 7, 2, 5, 0, 6, 0]])
'''

t0 = time.time()

startnum = puz > 0
print(startnum)
print(puz)
d1 = 0
r1 = 0
correct = 1
found = 1
while found > 0:
    found = 0
    while d1 < 9:
        if startnum[d1, r1] == False:
            print('Index: ', d1, r1)
            orig = puz[d1, r1]
            row = puz[d1, 0:9]
            col = puz[0:9, r1]
            if d1 < 3 and r1 < 3:
                block = puz[0:3, 0:3]
            elif d1 < 3 and 2 < r1 < 6:
                block = puz[0:3, 3:6]
            elif d1 < 3 and r1 > 5:
                block = puz[0:3, 6:9]
            elif 2 < d1 < 6 and r1 < 3:
                block = puz[3:6, 0:3]
            elif 2 < d1 < 6 and 2 < r1 < 6:
                block = puz[3:6, 3:6]
            elif 2 < d1 < 6 and r1 > 5:
                block = puz[3:6, 6:9]
            elif 5 < d1 and r1 < 3:
                block = puz[6:9, 0:3]
            elif 5 < d1 and 2 < r1 < 6:
                block = puz[6:9, 3:6]
            elif 5 < d1 and 5 < r1:
                block = puz[6:9, 6:9]
            else:
                print("Index not in bounds so cant find block")

            print('Column: \n', col, ' \nRow: \n', row, ' \nBlock: \n', block)
            print('Original:', orig)

            guess = 1
            poss = [0]
            howman = 0
            while guess < 10:
                if guess not in row and guess not in col and guess not in block and orig != guess:
                    poss.append(guess)
                    howman += 1
                guess += 1
            if howman == 1:
                found += 1
                puz[d1, r1] = poss[1]
        print(puz)
        if r1 < 8:
            r1 += 1
        else:
            d1 += 1
            r1 = 0

afterfirst = puz
print('Puzzle after first solve: \n', puz)

startnum = puz > 0
# Start algorithm
zer = 0
down = 0
right = 0
correct = 1
block = np.array(
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]])
# print(block)


while zer in puz:
    if startnum[down, right] == False:
        print('Index: ', down, right)
        orig = puz[down, right]
        row = puz[down, 0:9]
        col = puz[0:9, right]
        if down < 3 and right < 3:
            block = puz[0:3, 0:3]
        elif down < 3 and 2 < right < 6:
            block = puz[0:3, 3:6]
        elif down < 3 and right > 5:
            block = puz[0:3, 6:9]
        elif 2 < down < 6 and right < 3:
            block = puz[3:6, 0:3]
        elif 2 < down < 6 and 2 < right < 6:
            block = puz[3:6, 3:6]
        elif 2 < down < 6 and right > 5:
            block = puz[3:6, 6:9]
        elif 5 < down and right < 3:
            block = puz[6:9, 0:3]
        elif 5 < down and 2 < right < 6:
            block = puz[6:9, 3:6]
        elif 5 < down and 5 < right:
            block = puz[6:9, 6:9]
        else:
            print("Index not in bounds so cant find block")

        print('Column: \n', col, ' \nRow: \n', row, ' \nBlock: \n', block)
        print('Original:', orig)

        guess = 1
        poss = [0]
        howman = 0
        while guess < 10:
            if guess not in row and guess not in col and guess not in block and orig != guess:
                poss.append(guess)
                howman += 1
            guess += 1
        if howman > 0:
            correct = 1
            chooser = random.randint(howman) + 1
            puz[down, right] = poss[chooser]
        else:
            correct = 0
        if correct == 1:
            if right < 8:
                right += 1
            else:
                down += 1
                right = 0
        else:
            puz[down, right] = 0
            if right == 0:
                right = 8
                down -= 1
            else:
                right -= 1
        print(puz)
    else:
        if correct == 1:
            if right < 8:
                right = right + 1
            else:
                down = down + 1
                right = 0
        else:
            if right == 0:
                right = 8
                down = down - 1
            else:
                right = right - 1

print(puz)
t1 = time.time()
process = t1 - t0
print('Process Time: ', process)
