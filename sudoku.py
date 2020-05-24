'''
This program takes args from the command line
assuming the args passed in are sudoku puzzles
then solveing them
'''
import sys

class Sudoku:
    ''' wrapper class for a sudoku puzzle '''
    def __init__(self, file_in):
        self.puzzle = []
        self.orig = []
        # open the file with a temp fd
        with open(file_in, 'r') as fin:
            lines = fin.readlines()
            # process all the lines
            for line in lines:
                if line != "\n":
                    # no spaces and no nls
                    self.puzzle.append(
                        [c for c in line if c not in (' ', '\n')]
                        )
            # convert to nums
            for row in self.puzzle:
                for i, _ch in enumerate(row):
                    row[i] = 0 if _ch == '-' else int(_ch)
        self.orig = self.puzzle
    def print(self):
        ''' prints the current state of the puzzle '''
        for row in self.puzzle:
            print(row)
    def is_puzzle_valid(self):
        ''' ensures the stored puzzle is even solvable '''
        for i in range(0, 9):
            if not self.is_valid_row(i) or not self.is_valid_col(i):
                return False
        for i, j in [(i, j) for i in range(0, 7, 3) for j in range(0, 7, 3)]:
            if not self.is_valid_blk(i, j):
                return False
        return True
    def is_valid(self, row, col):
        ''' is the passed index valid '''
        return self.is_valid_row(row) and self.is_valid_col(col) and self.is_valid_blk(row, col)
    def is_valid_row(self, row):
        ''' checks a row and insures it is a valid row '''
        # all the non zero vals in the given row
        p_row = [i for i in self.puzzle[row] if i != 0]
        # culls the dupes
        return len(p_row) == len(set(p_row))
    def is_valid_col(self, col):
        ''' checks a col and insures it is a valid col '''
        # all the non zero vals in the given column
        p_col = [l[col] for l in self.puzzle if l[col] != 0]
        # culls the dupes
        return len(p_col) == len(set(p_col))
    def is_valid_blk(self, row, col):
        ''' checks a blk and insures it is a valid blk '''
        # calculate the block index
        r_blk = int(row / 3)
        c_blk = int(col / 3)
        # extrcat the block
        block = [r[3 * c_blk: 3 * (c_blk + 1)]
                 for r in self.puzzle[3 * r_blk:3 * (r_blk + 1)]]
        # take out all the zeros
        block = [val for sub in block for val in sub if val != 0]
        return len(block) == len(set(block))
    def solve(self):
        ''' solves the puzzle stored in the class '''
        if sud.is_puzzle_valid():
            if self.solve_rec(0, 0):
                print("succes!")
                self.print()
                return
            print("failure!")
        else:
            print("Puzzle is invalid!")
    def solve_rec(self, row, col):
        '''
        helper function to the main puzzle solver
        it operates recursively walking through the
        puzzle as it solves and walking back when
        wrong
        '''
        # calc the new rows and column
        if col >= 9:
            col = 0
            row = (row + 1)
        if self.puzzle[row][col] == 0:
            # test all the values for a cell
            for i in range(1, 10):
                self.puzzle[row][col] = i
                if self.is_valid(row, col):
                    # valid choice on the last cell
                    if row == 8 and col == 8:
                        return True
                    # recurse to the next cell and
                    # return the success of the call
                    if self.solve_rec(row, col + 1):
                        return True
            # undo what we have done
            self.puzzle[row][col] = 0
            return False
            # if it is a preset digit
            #and its the last on it is good
        if row == 8 and col == 8:
            return True
        # recurse down if is digit
        return self.solve_rec(row, col + 1)

# main exexution
if __name__ == '__main__':
    for a in sys.argv[1:]:
        print(a)
        sud = Sudoku(a) # init
        sud.print() # unsolved graph
        sud.solve() # solved graph
