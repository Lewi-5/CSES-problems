from typing import *


def solve(n: int) -> None:
    if n == 2 or n == 3:
        print("NO SOLUTION")
    else:
        evens_lst = [i for i in range(2, n+1, 2)]
        odds_lst = [i for i in range(1, n+1, 2)]

        evens_lst.extend(odds_lst)
        for x in evens_lst:
            print(x, end=" ")

def main():

    #test = 1

    #for i in range(1, 11):
        #file = open(f"tests/{test}.in")
        #n = int(file.readline())
        #file.close()
        #file = open(f"tests/{test}.out")
        #out = file.readline()
        #file.close()
        #print(f"expecting: {out}")
        #solve(n)
        #print()
        #test += 1


    n = int(input())
    solve(n)
main()

