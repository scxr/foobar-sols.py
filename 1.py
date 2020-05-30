"""

Input:
Solution.solution({14, 27, 1, 4, 2, 50, 3, 1}, {2, 4, -4, 3, 1, 1, 14, 27, 50})
Output:
    -4
 Given the lists  and y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
"""
x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]
if len(x) > len(y):
    print(list(set(x) - set(y))[0])
elif len(y) > len(x):
    print(list(set(y) - set(x))[0])
else:
    print(list(set(y) - set(x))[0])
