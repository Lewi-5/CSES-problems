from typing import *

def solve(seq: str) -> None:
    curr: int = 0
    lst_seq: List[int] = []
    for i in range(1,len(seq)):
        if seq[i] != seq[i - 1]:
            lst_seq.append(i - curr)
            curr = i
    lst_seq.append(len(seq[curr:]))
    print(max(lst_seq))


        
def main():
    s = input()

    solve(s)

main()
