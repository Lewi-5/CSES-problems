from typing import *

def print_vals(lst: List[int]) -> None:
    for x in lst:
        print(x, end=" ")
    print()

def solve(n:int) -> None:
    lst: List[int] = [i for i in range(1, n + 1)]
    sm = sum(lst)
    even: bool = sm % 2 == 0

    if not even:
        print("NO")
        return
    else:
        half: int = sm / 2
        half -= n
        first_set = [n]
        second_set = []
        # we already subtracted n so move the index one element back
        i = -2
        while half > 0:
            if lst[i] <= half:
                half -= lst[i]
                first_set.append(lst[i])
            else:
                second_set.append(lst[i])
            i -= 1
        # make sure to add 1 to include the element i left off at
        second_set.extend(lst[:i + 1])

        print("YES")
        print(len(first_set))
        print_vals(first_set)
        print(len(second_set))
        print_vals(second_set)

def main():
    n: int = int(input())

    solve(n)
main()

    
