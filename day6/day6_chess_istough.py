from collections import deque





def bfs(a, b, n):
    q = deque([(0, 0, 0)])
    direction = [[a, b], [-a, b], [-a, -b], [a, -b],
            [b, a], [-b, a], [-b, -a], [b, -a]]
    visited = [[False]*n for _ in range(n)]
   
    visited[0][0] = True
    while q:
        current_r, current_c, depth = q.popleft()

        depth += 1

        for dr, dc in direction:
            newrow = current_r + dr
            newcolumn = current_c + dc
            if check_limits(newrow, newcolumn, n) and not visited[newrow][newcolumn]:
                if newrow is n-1 and newcolumn is n-1:
                    return depth

                q.append((newrow, newcolumn, depth))
                visited[newrow][newcolumn] = True
    return -1
def check_limits(r, c, n):
    return 0 <= r < n and 0 <= c < n
def knightLmovt():
    n = int(input())

    fmove = [[0]*(n-1) for _ in range(n-1)]

    for i in range(1, n):
        for j in range(i, n):
            fmove[i-1][j-1] = bfs(i, j, n)
            fmove[j-1][i-1] = fmove[i-1][j-1]

    for final in fmove:
        print(*final)


knightLmovt()
