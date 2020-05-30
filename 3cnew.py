def solve(inp):
    cnt = 0
    for i in range(len(inp)):
        if inp[i] % inp[i+1] == 0:
            cnt +=1
        else:
            pass
        print(cnt)ils
solve([1, 2, 3, 4, 5, 6])
