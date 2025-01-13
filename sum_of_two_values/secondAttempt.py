from typing import *


# Second attempt, also too slow!


def solve(target: int, lst: List[int]) -> None:
    diff_lst: List[int] = []
    for i in range(0, len(lst)):
        if lst[i] in diff_lst:
            print(f"{i + 1} {diff_lst.index(lst[i]) + 1}")
            return
        else:
            diff_lst.append(target - lst[i])
    print("IMPOSSIBLE")

def main():
    first_inpt = list(map(int, input().split()))
    second_inpt = list(map(int, input().split()))
    solve(first_inpt[1], second_inpt)
main()

