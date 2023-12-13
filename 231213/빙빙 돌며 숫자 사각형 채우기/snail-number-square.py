# 행 , 열
n, m = tuple(map(int, input().split()))

S = [
    [0] * m
    for _ in range(n)
]

dirs = {
    # 행, 열
    0: [0, 1] ,
    1: [1, 0] ,
    2: [0, -1] ,
    3: [-1, 0]
}

def in_range(x, y, S):
    return (
        x >= 0 and x < m and y >= 0 and y < n
        and (S[x][y] == 0)
    )

n_dirs = 0
N = 1
S[0][0] = 1 
x, y = 0, 0
while N < m*n:
    N += 1
    nx, ny = x + dirs[n_dirs][0], y + dirs[n_dirs][1]
    if in_range(nx, ny, S):
        x, y= x + dirs[n_dirs][0], y + dirs[n_dirs][1]
        S[x][y] = N
        # print(x, y, S)
    else:
        n_dirs = (n_dirs + 1) % 4
        x, y = x + dirs[n_dirs][0], y + dirs[n_dirs][1]
        S[x][y] = N
        # print(x, y, S)

# for x in range(m):  # 열
#     for y in range(n):  # 행


for x in range(m):
    print(
        " ".join(list(map(str,S[x])))
        # S[x]
    )