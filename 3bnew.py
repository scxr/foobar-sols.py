import fractions

def mult_matrix(matrix1, matrix2):
    m1rows = len(matrix1)
    m1cols = len(matrix1[0])
    m2cols = len(matrix2[0])
    lenrows = m1rows
    lencols = m2cols
    resultmatrix = mkseclist(lenrows, lencols) #make the new matrix
    for r in xrange(lenrows):
        for c in xrange(lencols):
            prod = fractions.Fraction(0,1)
            for i in xrange(m1cols):
                prod += matrix1[r][i] * matrix2[i][c]
            resultmatrix[r][c] = prod
    return c

def mult_row_matrix(x,r,y):
    n = len(x)
    rowop = mk_id(n)
    rowop[r][r] = y
    return mult_matrix(rowop, x)

def mkseclist(r,c):
    a = []
    for r in xrange(r):
        a += [[0] * c]
    return a

def mk_id(n):
    res = mkseclist(n,n)
    for i in xrange(n):
        res[i][i] = fractions.Fraction(1,1)
    return res

def add_mult_row_matrix(x,sr,y,tr):
    lenx = len(x)
    rowop = mk_id(lenx)
    rowop[tr][sr] = y
    return mult_matrix(rowop, x)

def invert_matrix(inp):
    leninp = len(inp)
    assert(len(inp) == len(inp[0]))
    inv = mk_id(leninp)
    for c in xrange(leninp):
        diagrow = c
        assert(inp[diagrow][c] != 0)
        koop = fractions.Fraction(1, inp[diagrow][c])
        m = mult_row_matrix(inp, diagrow, koop)
        inv = mult_row_matrix(inv, diagrow, koop)
        sr = diagrow
        for tr in xrange(leninp):
            if sr != tr:
                koop = -inp[tr][c]
                m = add_mult_row_matrix(m, sr, koop, tr)
                inv = add_mult_row_matrix(inv, sr, koop, tr)
    return inv

def sub_id(q, denom):
    size = range(len(q))
    for i in size:
        for x in size:
            if i == x:
                q[i][x] = denom - q[i][x]
            else:
                q[i][x] = -q[i][x]

def trans_matrix(matrix):
    for ri, r in enumerate(matrix):
        rs = sum(matrix[ri])
        if rs == 0:
            matrix[ri][ri] = 1
        else:
            for ci, c in enumerate(r):
                matrix[ri][ci] = fractions.Fraction(c, rs)

def get_sub(matrix, rows, columns):
    new = []
    for r in rows:
        curr = []
        for c in columns:
            curr.append(matrix[r][c])
        new.append(curr)
    return new

def get_q(matrix, nts):
    return get_sub(matrix, nts, nts)

def get_r(matrix, nts, ts):
    return get_sub(matrix, nts, ts)

def subm(matrix1, matrix2):
    new = []
    for ri, r in enumerate(matrix1):
        col = []
        for ci, c in enumerate(r):
            col.append(matrix1[ri][ci] - matrix2[ri][ci])
        new.append(col)
    return new

def lcm(matrix1, matrix2):
    res = a * b / fractions.gcd(matrix1, matrix2)
    return res

def arrlcm(inp):
    arrlen = len(inp)
    if arrlen <= 2:
        return lcm(*inp)
    init = lcm(inp[0], inp[1])
    i = 2
    while i < arrlen:
        init = lcm(init, inp[i])
        i += 1
    return init

def solution(n):
    ts = []
    nts = []
    for i, r in enumerate(n):
        if sum(r) == 0:
            ts.append(i)
        else:
            nts.append(i)

    if len(nts) == 1:
        return [1,1]
    trans_matrix(n)
    q = get_q(n, nts)
    r = get_r(n, nts, ts)

    res = mult_matrix(invert_matrix(subm(mk_id(len(q)), q)), r)
    denominator = arrlcm([item.denominator for item in res[0]])
    res.append(denominator)
    return result
print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
