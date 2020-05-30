
import json
import math
"""
https://en.wikipedia.org/wiki/Partition_(number_theory)
"""
def solution(n):
    # pad size
    sizearr = n + 1

    # create zero-filled multi_arr
    multi_arr = [[0 for x in xrange(sizearr)] for n in xrange(sizearr)]

    # base value is always skipped after being padded
    multi_arr[0][0] = 1
    for last in xrange(1, sizearr):
        for next in xrange(0, sizearr):
            multi_arr[last][next] = multi_arr[last - 1][next]
            if next >= last:
                multi_arr[last][next] += multi_arr[last - 1][next - last]

    return multi_arr[n][n] - 1
print solution(200)
