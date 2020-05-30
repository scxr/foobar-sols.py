import math
def dist_vector(size, start, tot_length, length):
    temp = [start]
    cnt = 0
    l, r = -length, tot_length - length
    for i in range(size):
        lft = temp[0]
        right = temp[cnt]
        lft += (l*2)
        right += (r*2)
        l, r = -r,-l
        temp = [lft] + temp + [right]
        cnt += 2
    return temp

def make_matrix(vector1, vector2):
    matrix = []
    cnt = 0
    for i in vector2:
        matrix.append([])
        for j in vector1:
            matrix[cnt].append((j,i))
        cnt += 1
    return matrix

def translate(x, y, vector):
    matrix = []
    cnt = 0
    for i in vector:
        matrix.append([])
        for j in i:
            matrix[cnt].append((j[0] + x, j[1] + y))
        # print mat[cnt]
        cnt += 1

    return matrix

def serialize(vector):
    start = int(len(vector)/ 2)
    elements = [vector[start][start]]
    cnt = 3
    start -= 1
    while( start >= 0):
        x = start
        y = start
        for j in range(1, cnt):
            x+= 1
            elements+= [vector[y][x]]
        for j in range(1, cnt):
            y+= 1
            elements+= [vector[y][x]]
        for j in range(1, cnt):
            x-= 1
            elements+= [vector[y][x]]
        for j in range(1, cnt):
            y-= 1
            elements+= [vector[y][x]]

        start -= 1
        cnt += 2
    return elements

def key(x,y):
    return format(math.atan2(x,y),'.32f')


def dist(x,y):
    return math.hypot(x,y)

def calc(cap,bad, distance):
    visited = {}
    l = len(cap)
    cnt  = 0
    for i in range(l):
        captain_elements = cap[i]
        badguy_elements = bad[i]

        visited[key(captain_elements[0], captain_elements[1])] = True
        if distance - dist(badguy_elements[0], badguy_elements[1]) >=0 :
            k = key(badguy_elements[0], badguy_elements[1])
            if k not in visited:
                cnt += 1
                visited[k] = True
        else:
            k = key(badguy_elements[0], badguy_elements[1])
            visited[k] = True
    return cnt




def answer(dimensions, captain, badguy, distance):
    x = 0
    y = 1
    tx = captain[x]
    ty = captain[y]
    width = dimensions[0]
    height = dimensions[1]
    mat_size = int(math.ceil(max( distance/width, distance / height))) + 1
    badx =  dist_vector(mat_size, badguy[x],width,badguy[x])
    bady =  dist_vector(mat_size, badguy[y],height,badguy[y])
    capx =  dist_vector(mat_size, captain[x],width,captain[x])
    capy =  dist_vector(mat_size, captain[y],height,captain[y])
    #print 'here'
    elms_bad =  serialize(translate(-tx, -ty, make_matrix(badx, bady)))
    elms_cap =  serialize(translate(-tx, -ty, make_matrix(capx, capy)))
    #print 'oop'
    #print '\n\n\n\n\n\n\n\n\n\n\n\n'
    return calc(elms_cap, elms_bad, distance)

print(answer([300,275], [150,150], [185,100], 500))
