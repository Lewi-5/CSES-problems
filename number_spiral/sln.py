from typing import *


def solve(row: int, col: int) -> None:
    if col == 1 and row == 1:
        print(1)
        return
    


    row_head:int = row ** 2 if row % 2 == 0 else  ((row - 1) ** 2) + 1
    col_head:int = col ** 2 if col % 2 != 0 else  ((col - 1) ** 2) + 1
    
    if col == 1:
        print(row_head)
        return
    if row == 1:
        print(col_head)
        return

    # if row == col, row is even means row_head > col_head, row is odd col_head > row_head
    # otherwise choose the max of row, col
    # if the head of the max is a perfect square, count down min of row, col times
    # if the head of the max not a perfect square, count up min of row,col times

    if row == col:
        num: int = row_head - (col - 1) if row % 2 == 0 else col_head - (row - 1)
        print(num)
    else:
        if row > col:
            num: int = row_head - (col - 1) if row % 2 == 0 else row_head + (col - 1)
            print(num)
        else:
            num: int = col_head - (row - 1) if col % 2 != 0 else col_head + (row - 1)
            print(num)

def main():
    tests: int = int(input())

    for i in range(0, tests):
        point: List[str] = input().split(" ")
        row: int = int(point[0]) 
        col: int = int(point[1])
        solve(row, col)
main()
        





