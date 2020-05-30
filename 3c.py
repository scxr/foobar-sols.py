def solution(tripletlist):
    newarr = [0] * len(tripletlist) # create an empty array the size of tl
    cnt = 0 # init our output
    for i in range(0,len(tripletlist)):
        for j in range(0, i):
            if tripletlist[i] % tripletlist[j] == 0: # if theyre divisible
                newarr[i] += 1 # add to our new array
                cnt += newarr[j] # completed
    return cnt # answer
print(solution([1, 1,1]))
