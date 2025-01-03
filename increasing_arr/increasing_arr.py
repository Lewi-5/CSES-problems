from typing import *


def solve(lst: List[int]) -> None:
    moves: int = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            moves += lst[i - 1] - lst[i]
            lst[i] = lst[i - 1]
    print(moves)

def main():
    q = input()
    lst = input()

    lst = list(map(lambda num: int(num), lst.split(" ")))



    solve(lst)


main()

        