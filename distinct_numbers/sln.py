from typing import *


def solve(lst: List[int]) -> None:
    lst.sort()
    count = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            count += 1
    print(count)

def main():
    input()
    lst = list(map(int,input().split()))


    solve(lst)
main()