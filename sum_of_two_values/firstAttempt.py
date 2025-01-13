from typing import *

# DOES NOT WORK fast enough, need to find another solution

def solve(target: int, lst: List[int]) -> None:
    for i in range(0, len(lst)):
        diff: int = target - lst[i]
        #print(diff)
        #print(f"diff in lst: {diff in lst}")
        #print(f"iteration: {i} , index of diff: {"none" if diff not in lst else lst.index(diff)}")
        idx_summand: int | None = None if diff not in lst else lst.index(diff) 
        #print(idx_summand)
        if idx_summand is not None and idx_summand != i:
            print(f"{i + 1} {idx_summand + 1}")
            return
    print("IMPOSSIBLE")


def main():
    first_inpt = list(map(int, input().split()))
    second_inpt = list(map(int, input().split()))
    solve(first_inpt[1], second_inpt)
main()


        
        
