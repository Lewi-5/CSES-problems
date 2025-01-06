from typing import *


def solve(n: int) -> None:
    factor: int = 5
    number_of_five_prime_factors: int = 0
    while factor <= n:
        number_of_five_prime_factors += n // factor
        factor *= 5
    print(number_of_five_prime_factors)



    
def main():
    n = int(input())

    solve(n)

main()
