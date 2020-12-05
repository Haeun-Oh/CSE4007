from heapq import heappush, heappop
from queue import Queue
import copy

def ShortestPath(parent, goal, matrix):
    node = goal
    while parent[node[0]][node[1]] != node:
        if matrix[node[0]][node[1]] == 2 or matrix[node[0]][node[1]] == 6:
            matrix[node[0]][node[1]] = 5

        node = parent[node[0]][node[1]]

def Uniformed_explore(starting, matrix, key):
    map = copy.deepcopy(matrix)
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    pos = []
    que = Queue()
    time =0
    for i in range(0, m):
        pos.append([(i, x) for x in range(0, n)])

    que.put((starting, 0, starting))
    while not que.empty():
        node = que.get()
        now, ex_length, parent = node

        pos[now[0]][now[1]] = parent
        map[now[0]][now[1]] = 1

        if matrix[now[0]][now[1]] == 6:
            ShortestPath(pos, now, matrix)
            key.append(now)
            return (time, ex_length, now, key)

        for i in range(4):
            nowy = now[0] + dy[i]
            nowx = now[1] + dx[i]
            if nowx < 0 or nowy < 0 or nowx >= n or nowy >= m:
                continue
            if map[nowy][nowx] != 1:
                mv = (nowy, nowx)
                que.put((mv, ex_length + 1, now))
        time = time + 1
    return (0, 0, now, key)

def Uniformed_end(starting, matrix):
    map = copy.deepcopy(matrix)
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    pos = []
    que = Queue()
    time=0
    for i in range(0, m):
        pos.append([(i, x) for x in range(0, n)])

    que.put((starting, 0, starting))
    while not que.empty():
        node = que.get()
        now, ex_length, parent = node

        pos[now[0]][now[1]] = parent
        map[now[0]][now[1]] = 1

        if now == arrive:
            ShortestPath(pos, arrive, matrix)
            return (time, ex_length)

        for i in range(4):
            nowy = now[0] + dy[i]
            nowx = now[1] + dx[i]
            if nowx < 0 or nowy < 0 or nowx >= n or nowy >= m:
                continue
            if map[nowy][nowx]!=1:
                mv = (nowy, nowx)
                que.put((mv, ex_length + 1, now))
        time = time + 1
    return (0, 0)

def bfs(matrix):
    bfs_time = 0
    bfs_length = 0
    bfs_key = []
    pos = start
    while len(bfs_key) != all_key:
        r = Uniformed_explore(pos, matrix, bfs_key)
        bfs_time += r[0]
        bfs_length += r[1]
        pos = r[2]
        bfs_key = r[3]

    r = Uniformed_end(pos, matrix)
    bfs_time += r[0]
    bfs_length += r[1]

    output = str()
    for row in matrix:
        for point in row:
            output = output + str(point) + ''
        output += '\n'
    output += '---\nlength=' + str(bfs_length) + '\ntime=' + str(bfs_time) + '\n'

    with open('Maze_%d_BFS_output.txt' % k, 'w') as f:
        f.writelines(output)
    for i in range(0, m):
        for j in range(0, n):
            if (i, j) in bfs_key:
                matrix[i][j]=6
            if matrix[i][j] == 5:
                matrix[i][j]=2

#######################################################
def dfs(starting, matrix, key, limit):
    map = copy.deepcopy(matrix)
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    pos = []
    stack = []
    time = 0
    depth = 0
    for i in range(0, m):
        pos.append([(i, x) for x in range(0, n)])

    stack.append((starting, 0, starting))
    while (stack):
        if depth >limit:
            return (time, 0, False, now, key)
        node = stack.pop()
        now, ex_length, parent = node

        pos[now[0]][now[1]] = parent
        map[now[0]][now[1]] = 1

        if matrix[now[0]][now[1]] == 6:
            ShortestPath(pos, now, matrix)
            key.append(now)
            return (time, ex_length, True, now, key)

        for i in range(4):
            nowy = now[0] + dy[i]
            nowx = now[1] + dx[i]
            if nowx < 0 or nowy < 0 or nowx >= n or nowy >= m:
                continue
            if map[nowy][nowx] != 1:
                mv = (nowy, nowx)
                stack.append((mv, ex_length + 1, now))
        time = time + 1
        depth +=1
    return (time, 0, False, now, key)

def dfs_arrive(starting, matrix, limit):
    map = copy.deepcopy(matrix)
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    pos = []
    stack = []
    time = 0
    depth = 0
    for i in range(0, m):
        pos.append([(i, x) for x in range(0, n)])

    stack.append((starting, 0, starting))
    while (stack):
        if depth >limit:
            return (time, 0, False, now)
        node = stack.pop()
        now, ex_length, parent = node

        pos[now[0]][now[1]] = parent
        map[now[0]][now[1]] = 1

        if matrix[now[0]][now[1]] == 4:
            ShortestPath(pos, now, matrix)
            return (time, ex_length, True, now)

        for i in range(4):
            nowy = now[0] + dy[i]
            nowx = now[1] + dx[i]
            if nowx < 0 or nowy < 0 or nowx >= n or nowy >= m:
                continue
            if map[nowy][nowx] != 1:
                mv = (nowy, nowx)
                stack.append((mv, ex_length + 1, now))
        time = time + 1
        depth +=1
    return (time, 0, False, now)

def ids(matrix):
    ids_time = 0
    ids_length = 0
    ids_key = []
    maxDepth = 0
    pos = start
    while len(ids_key) != all_key:
        r = dfs(pos, matrix, ids_key, maxDepth)
        ids_time += r[0]
        if r[2]==False:
            maxDepth+=1
        else:
            ids_length += r[1]
            pos = r[3]
            ids_key = r[4]
    while pos != arrive:
        r = dfs_arrive(pos, matrix, maxDepth)
        ids_time += r[0]
        if r[2] == False:
            maxDepth += 1
        else:
            ids_length += r[1]
            pos = r[3]

    output = str()
    for row in matrix:
        for point in row:
            output = output + str(point) + ''
        output += '\n'
    output += '---\nlength=' + str(ids_length) + '\ntime=' + str(ids_time) + '\n'

    with open('Maze_%d_IDS_output.txt' % k, 'w') as f:
        f.writelines(output)
    for i in range(0, m):
        for j in range(0, n):
            if (i, j) in ids_key:
                matrix[i][j]=6
            if matrix[i][j] == 5:
                matrix[i][j]=2

#################################################################
def Informed_explore(starting, matrix, arrive, heuristic):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    map = copy.deepcopy(matrix)
    heap = []
    time = 0
    pos = []

    for i in range(0, m):
        pos.append([(i, x) for x in range(0, n)])

    heappush(heap, (0, (starting, 0, starting)))
    while (len(heap)>0):
        now, ex_length, parent = heappop(heap)[1]

        pos[now[0]][now[1]] = parent
        map[now[0]][now[1]] = 1

        if now == arrive:
            node = arrive
            while pos[node[0]][node[1]] != node:
                if matrix[node[0]][node[1]] == 2 or matrix[node[0]][node[1]] == 6:
                    matrix[node[0]][node[1]] = 5

                node = pos[node[0]][node[1]]

            return (time, ex_length)

        for i in range(4):
            nowy = now[0] + dy[i]
            nowx = now[1] + dx[i]
            if nowx < 0 or nowy < 0 or nowx >= n or nowy >= m:
                continue
            if map[nowy][nowx]!=1:
                mv = (nowy, nowx)
                heappush(heap, (heuristic(now, arrive, ex_length + 1), (mv, ex_length + 1, now)))
        time = time + 1
    return (0, 0)

def gbfs(matrix):
    global all_key, start
    heuristic = lambda a, b, c: abs(a[0] - b[0]) + abs(a[1] - b[1])
    find_key.sort(key=lambda x: [x[1], x[0]])
    gbfs_time = 0
    gbfs_length = 0

    exp = Informed_explore(start, matrix, find_key[0], heuristic)
    gbfs_time += exp[0]
    gbfs_length += exp[1]

    for i in range(0, all_key - 1):
        exp = Informed_explore(find_key[i], matrix, find_key[i + 1], heuristic)
        gbfs_time += exp[0]
        gbfs_length += exp[1]

    exp = Informed_explore(find_key[all_key - 1], matrix, arrive, heuristic)
    gbfs_time += exp[0]
    gbfs_length += exp[1]

    output = str()
    for row in matrix:
        for point in row:
            output = output + str(point) + ''
        output += '\n'
    output += '---\nlength=' + str(gbfs_length) + '\ntime=' + str(gbfs_time) + '\n'

    with open('Maze_%d_GBFS_output.txt' % k, 'w') as f:
        f.writelines(output)
    for i in range(0, m):
        for j in range(0, n):
            if (i, j) in find_key:
                matrix[i][j] = 6
            if matrix[i][j] == 5:
                matrix[i][j] = 2

def a_star(matrix):
    global all_key, start
    heuristic = lambda a, b, c: abs(a[0] - b[0]) + abs(a[1] - b[1]) + c
    find_key.sort(key=lambda x: [x[1], x[0]])
    astar_time = 0
    astar_length = 0

    exp = Informed_explore(start, matrix, find_key[0], heuristic)
    astar_time += exp[0]
    astar_length += exp[1]

    for i in range(0, all_key - 1):
        exp = Informed_explore(find_key[i], matrix, find_key[i + 1], heuristic)
        astar_time += exp[0]
        astar_length += exp[1]

    exp = Informed_explore(find_key[all_key - 1], matrix, arrive, heuristic)
    astar_time += exp[0]
    astar_length += exp[1]

    output = str()
    for row in matrix:
        for point in row:
            output = output + str(point) + ''
        output += '\n'
    output += '---\nlength=' + str(astar_length) + '\ntime=' + str(astar_time) + '\n'

    with open('Maze_%d_A_star_output.txt' % k, 'w') as f:
        f.writelines(output)
    for i in range(0, m):
        for j in range(0, n):
            if (i, j) in find_key:
                matrix[i][j]=6
            if matrix[i][j] == 5:
                matrix[i][j]=2

######################################

def main():
    global k, n, m, start, find_key, first, arrive, informed_start, all_key
    f = open('Maze_1.txt', 'r')
    first = f.readline()
    input = first.split()
    k = int(input[0])
    m = int(input[1])
    n = int(input[2])
    matrix = []
    start = ()
    arrive = ()
    find_key = []
    all_key = 0
    for i in range(0, m):
        a = list(f.readline())
        a = a[:-1]
        a = list(map(int, a))
        matrix.append(a)
    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 3:
                start = (i, j)
            elif matrix[i][j] == 6:
                find_key.append((i, j))
                all_key +=1
            elif matrix[i][j]==4:
                arrive = (i, j)
    bfs(matrix)
    ids(matrix)
    gbfs(matrix)
    a_star(matrix)

    f.close()

if __name__ == "__main__":
    main()
