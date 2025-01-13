

def solve(target, lst):
    # we can exit early if the sum searched for is impossible to create from the summands available
    if target <= 1 or target > sum(lst):
        print("IMPOSSIBLE")
        return
    dic = dict()
    for i in range(0, len(lst)):
        curr_val = lst[i]
        complement = target - curr_val
        if dic.get(complement) is not None:
            print(f"{dic[complement] + 1} {i + 1}")
            return
        else:
            dic[curr_val] = i
    print("IMPOSSIBLE")



def main():
    first_inpt = list(map(int, input().split()))
    second_inpt = list(map(int, input().split()))
    solve(first_inpt[1], second_inpt)
main()