from typing import *

# attempted with binary search, still too slow...

def binary_search(value: int, lst: List[int]) -> int:
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (high + low ) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1 

def get_last_index(value: int, lst: List[int]) -> int:
    lst_length = len(lst)
    for i in range(lst_length - 1, -1, -1):
        if lst[i] == value:
            return i
    return -1


def solve(target: int, lst: List[int]) -> None:
    sorted_lst = sorted(lst)
    for i in range(0, len(lst)):
        complement = target - lst[i]
        last_index_complement = get_last_index(complement, lst)
        if binary_search(complement, sorted_lst) != -1 and last_index_complement != i:
            print(f"{i + 1} {last_index_complement + 1}")
            return
    print("IMPOSSIBLE")


def main():
    first_inpt = list(map(int, input().split()))
    second_inpt = list(map(int, input().split()))
    solve(first_inpt[1], second_inpt)
main()

