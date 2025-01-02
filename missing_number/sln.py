from typing import *

# this solution using reduce was much faster than my first implementation using filter
def solve_red(n: int, lst: List[int]) -> None:
    complete_sum = sum([i for i in range(0, n + 1)])
    inpt_sum = sum(lst)
    print(f"{complete_sum - inpt_sum}")
# this works for smaller  cases but fails to complete in less than 1s for n > 100000
def solve(n: int, lst: List[int]) -> None:
    complete_lst: List[int] = [i for i in range(1, n + 1)]
    filtered_lst: List[int] = list(filter(lambda elem: elem not in lst, complete_lst))
    print(f"{filtered_lst[0]}")

def main():

    #filen = 14

    #f = open(f"tests/{filen}.in", "r")
    #n = f.readline()
    #lst = f.readline()

    #f.close()

    #f = open(f"tests/{filen}.out", "r")
    #print("expecting: ")
    #print(f.readline())
    #f.close()

    n = input()
    lst = input()



    lst = list(map(lambda s: int(s), lst.split(" ")))

    solve_red(int(n), lst)

main()
