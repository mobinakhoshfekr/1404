def Maze(maze, start, goal):
    n = len(maze)
    if n > 0:
        m = len(maze[0])
    else:
        m = 0

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def isBlocked(row, column):
        if row < 0 or column < 0 or row >= n or column >= m:
            return True
        return maze[row][column] == 1

    if start == goal:
        return [start]

    stack = []

    i, j = start
    dir = 0

    maze[i][j] = 1

    while True:
        d_r, d_c = directions[dir]
        s = i + d_r
        k = j + d_c

        if isBlocked(s, k):
            dir += 1
            if dir < 8:
                continue
            else:
                if not stack:
                    return None
                prev_i, prev_j, prev_dir = stack.pop()
                i, j = prev_i, prev_j
                dir = prev_dir + 1
                continue

        else:
            stack.append((i, j, dir))
            i, j = s, k
            maze[i][j] = 1
            if (i, j) == goal:
                path = []
                for r, c, dir in stack:
                    path.append((r, c))
                path.append((i, j))
                stack.clear()
                return path
            dir = 0
            continue
            

if __name__ == "__main__":
    maze = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    start = (1, 1)
    goal = (3, 4)

    path = Maze(maze, start, goal)
    if path is None:
        print("بن‌بست!")
    else:
        print("مسیر:")
        for i in path:
            print(i)