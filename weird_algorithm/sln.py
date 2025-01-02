from typing import *
# i initially thought that CSES would pass arguments in at the command line, but it
# seems like they just read the argument from stdin
#import argparse 


'''
Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
$$ 3 rightarrow 10 rightarrow 5 rightarrow 16 rightarrow 8 rightarrow 4 rightarrow 2 rightarrow 1$$
Your task is to simulate the execution of the algorithm for a given value of n.
Input
The only input line contains an integer n.
Output
Print a line that contains all values of n during the algorithm.
Constraints

1 le n le 10^6

Example
Input:
3

Output:
3 10 5 16 8 4 2 1
'''

def solve(n: int) -> None:
    print(f"{n}", end = " ")
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3*n) + 1
        print(f"{int(n)}", end = " ")

def main():
    n = input()
    solve(int(n))
'''
# see comments above the import argparse above
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n")

    args = parser.parse_args()

    main(args.n)
'''
main()
