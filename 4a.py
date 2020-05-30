import itertools

def solution(t, t_l): # pray to the holy gods it passed
    num = len(t) - 2
    bi = [b + 1 for b in xrange(num)]
    distance = bellford(t)
    if neg(distance):
        return range(num)
    for w in xrange(num, 0, -1):
        for i in itertools.permutations(bi, w):
            cost = getcost(i, distance)
            if cost <= t_l:
                return [b - 1 for b in sorted(i)]

def getcost(b, distance): # get the cost between two points
    cost = 0
    for i in xrange(0, len(b) - 1):
        curr = b[i]
        next = b[i + 1]
        cost += distance[curr][next]
    start = 0
    finish = len(distance) - 1
    cost += distance[start][b[0]]
    cost += distance[b[-1]][finish]
    return cost

def bellford(vortex): # get the total bellman ford values
    distance = []
    for vertex in range(len(vortex)):
        distances = single_bellford(vortex, vertex)
        distance.append(distances)
    return distance

def single_bellford(vortex, start): #bellman for for specific set
    distances = [float('inf') for vertex in vortex]
    distances[start] = vortex[start][start]
    for i in range(len(vortex)):
        for u, v, weight in enumedge(vortex):
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    return distances

def enumedge(vortex): # enumerate the different edges
    for u, row in enumerate(vortex):
        for v, weight in enumerate(row):
            yield (u, v, weight)

def neg(bfmatrix): # this checks if there is a negative cycle
    distances = bfmatrix[0]
    for u, v, weight in enumedge(bfmatrix):
        if distances[u] + weight < distances[v]:
            return True
    return False
