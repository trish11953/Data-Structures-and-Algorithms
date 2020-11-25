############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Trisha Mandal"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

from random import random
import copy
from collections import deque
from math import factorial as fact


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    result = fact(n ** 2) / fact(n ** 2 - n) / fact(n)
    return result


def num_placements_one_per_row(n):
    result = n ** n
    return result


def n_queens_valid(board):
    offset = 0
    for a in board:
        for b in range(0, offset):
            off = offset - b
            x = board[b]
            y = board[b] + off
            z = board[b] - off
            if a == x or a == y or a == z:
                return False
        offset = offset + 1
    return True


def n_queens_helper(n, board=()):
    for a in range(0, n):
        valid = n_queens_valid(board + (a,))
        if valid:
            if len(board) == n - 1:
                yield [a]
            if len(board) != n - 1:
                for r in n_queens_helper(n, board + (a,)):
                    yield [a] + r


def n_queens_solutions(n):
    result = list(n_queens_helper(n))
    return result


############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board
        self.rownum = len(self.board)
        self.columnnum = len(self.board[0])

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        self.board[row][col] = not self.board[row][col]

        if col > 0:
            self.board[row][col - 1] = not self.board[row][col - 1]
        if row > 0:
            self.board[row - 1][col] = not self.board[row - 1][col]
        if row < self.rownum - 1:
            self.board[row + 1][col] = not self.board[row + 1][col]
        if col < self.columnnum - 1:
            self.board[row][col + 1] = not self.board[row][col + 1]

    def scramble(self):
        for a in range(self.rownum):
            for b in range(self.columnnum):
                if random() < 0.5:
                    self.perform_move(a, b)

    def is_solved(self):
        for a in range(0, self.rownum):
            for b in range(0, self.columnnum):
                if self.board[a][b]:
                    return False
        return True

    def copy(self):
        result = copy.deepcopy(self)
        return result

    def successors(self):
        for a in range(0,self.rownum):
            for b in range(0,self.columnnum):
                new = self.copy()
                new.perform_move(a, b)
                yield (a, b), new

    def find_solution(self):
        sequence, boards = [], []
        num = len(deque([(sequence, self)]))
        level = deque([(sequence, self)])
        newset = set()
        while num >= 1:
            present = level.popleft()
            temptuple = tuple(tuple(a) for a in present[1].get_board())
            newset.add(temptuple)
            for a, b in present[1].successors():
                case = 0
                path = present[0] + [a]
                condition =tuple(tuple(a) for a in b.get_board()) not in newset
                if condition:
                    case = 1
                if b.is_solved():
                    case = 2
                if case == 1:
                    if b.get_board() not in boards:
                        boards.append(b.get_board())
                        level.append((path, b))
                if case == 2:
                    return path
        return None


def create_puzzle(rows, cols):
    resultboard = [[False for a in range(0, cols)] for b in range(0, rows)]
    result = LightsOutPuzzle(resultboard)
    return result


############################################################
# Section 3: Linear Disk Movement
############################################################

def next_move(celllist, length):
    for a in range(0, length):
        if a + 1 < length and a + 2 < length:
            if celllist[a] == 1:
                if celllist[a + 1] == 1:
                    if celllist[a + 2] == 0:
                        celllist[a], celllist[a + 2] = celllist[a + 2], celllist[a]
                        yield (a, a + 2), celllist
                        celllist = copy.deepcopy(celllist)
                elif celllist[a + 1] == 0:
                    celllist[a], celllist[a + 1] = celllist[a + 1], celllist[a]
                    yield (a, a + 1), celllist
                    celllist = copy.deepcopy(celllist)

#used the deque psuedo code to write this code
def solve_identical_disks(length, n):
    start, end = [], []
    for i in range(0, length):
        if i < n:
            start = start + [1]
        else:
            start = start + [0]
    for i in range(0, length):
        if i < length - n:
            end = end + [0]
        else:
            end = end + [1]

    sequence = []
    front = deque([(sequence, start)])
    newset, presentpath = set(), set()

    while len(deque([(sequence, start)])) >= 1:
        present = front.popleft()
        newset.add(tuple(present[1]))
        for a, b in next_move(present[1], length):
            if start == end:
                return present[0] + [a]
            if tuple(b) not in newset:
                if tuple(b) not in presentpath:
                    front.append((present[0] + [a], b))
                    presentpath.add(tuple(b))
    return None


def solve_distinct_disks(length, n):
    pass


############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
I took around 18 hours to do this assignment. 
"""

feedback_question_2 = """
Section 3 was the hardest out of all of them. 
It was very difficult for me to figure out the logic. 
I left it incomplete because I couldn't come up with it.
"""

feedback_question_3 = """
I think this assignment made me think a lot and i came up with creative ways to solve it.
But I also think that the difficulty was alot and not everyone can come up with the solution.
"""
