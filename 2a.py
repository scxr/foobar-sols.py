"""
There are 4 key rules which you must follow in order to avoid a revolt:
    1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.)
    2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
    3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.
    (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.
    The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.)
    4. You can always find more henchmen to pay - the Commander has plenty of employees.
    If there are enough LAMBs left over such that another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.

Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.
"""
def solution(total_lambs):
    if total_lambs > 10**9:
        return 0 # out of bounds
    """
    powers of 2’s sum
    """
    dl = []
    a = 0
    tot = 0
    while a<=total_lambs:
        curr = 2**a
        dl.append(curr)
        tot += curr
        if tot > total_lambs:
            break
        a += 1

    """
    Fibonnaci sequence
    The next number is found by adding up the two numbers before it.
    """
    fibolist = [1,1]
    fibotot = 2
    b = 2
    while b <= total_lambs:
        fibval = fibolist[b-1] + fibolist[b-2]
        fibolist.append(fibval)
        fibotot += int(fibolist[b])
        if fibotot > total_lambs:
            break
        b += 1
    ans = len(fibolist) - len(dl)
    return abs(ans)



print(answer(int(input())))
