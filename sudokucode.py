import copy

def check(puzzle, num, r, c):
    #checks row r for duplicates of num
    count = 0
    for i in range(0,9):
        if puzzle[r][i] == num:
            count = count + 1
        if count > 1:
            return False
    #checks column c for duplicates of num
    count = 0
    for i in range(0,9):
        if puzzle[i][c] == num:
            count = count + 1
        if count > 1:
            return False
    #checks subgrid of r,c for duplicates of num
    count = 0
    subrow = (r//3)*3
    subcolumn = (c//3)*3
    for r in range(subrow,subrow+3):
        for c in range(subcolumn,(subcolumn)+3):
            if puzzle[r][c] == num:
                count = count + 1
            if count > 1:
                return False
    #returns True if no duplicates are found
    return True

def backwards(empty,r,c):
    #returns r,c of last empty cell
    if c < 0 or c == 0 and empty[r][c]!= 0:
        r = r - 1
        c = 8
        return backwards(empty,r,c)
    elif empty[r][c] != 0:
        c = c - 1
        return backwards(empty,r,c)
    elif empty[r][c] == 0:
        return r,c

def sudoku(puzzle):
    #creates copy of empty puzzle and loops through rows, then columns
    empty = copy.deepcopy(puzzle)
    r = 0
    while r <= len(puzzle)-1:
        fillin = 1
        c = 0
        while c <= len(puzzle[r])-1:
            #if cell is full, skips cell
            if empty[r][c] != 0:
                c += 1
                continue
            #if all values are attempted, empty cell and continue fill in count on closest previous cell"""
            if fillin > 9:
                puzzle[r][c] = 0
                r,c = backwards(empty,r,c-1)
                fillin = puzzle[r][c] + 1
                continue
            #fills cell with fill in value
            if empty[r][c] == 0:
                puzzle[r][c] = fillin
            #if the fill in value fails check, continues counting in same cell
            if not check(puzzle,puzzle[r][c],r,c):
                fillin += 1
                continue
            #resets fill in value and moves to next free cell if viable number was found
            fillin = 1
            c += 1
        r += 1
    return puzzle
