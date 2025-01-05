from typing import *

def solve(s: str) -> None:
    dic = dict()
    for char in s:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    # check number of single occurring letters
    num_odd = 0
    odd = ""
    even = []
    for key in dic:
        if dic[key] % 2 != 0:
            num_odd += 1
            odd = key
            if num_odd > 1:
                print("NO SOLUTION")
                return
        else:
            even.append(key)
    half = [key * (dic[key]//2) for key in even]
    odd_lst = []
    if odd in dic:
        odd_lst = [odd * dic[odd]]
    print("".join([*half,*odd_lst,*half[::-1]]))

def main():
    s = input()
    solve(s)
main()