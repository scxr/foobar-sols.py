from fractions import Fraction

def solution(pegs):
    lenarr = len(pegs)
    if not(pegs) or lenarr == 1:
        return [-1,-1]

    if lenarr % 2 == 0:
        iseven = True
    else:
        iseven = False

    if iseven:
        sum = (-pegs[0] + pegs[lenarr -1])
    else:
        sum = (- pegs[0] - pegs[lenarr -1])

    if lenarr > 2:
        for i in xrange(1, lenarr -1):
            sum += 2 * (-1)**(i+1) * pegs[i]
    if iseven:
        first = Fraction(2 * (float(sum)/3))
    else:
        first = Fraction(2 * sum)

    first = first.limit_denominator()

    curr = first
    for i in range(0, lenarr -2):
        centre = pegs[i+1] - pegs[i]
        nextr = centre - curr
        if curr < 1 or nextr < 1:
            return [-1,-1]
        else:
            curr = nextr
    return(first.numerator, first.denominator)


print(solution([4, 30, 50]))
