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

def in_range(x, y):
    return (
        x >= 0 and x < n and y >= 0 and y < m
    )

n_dirs = 0
N = 1
S[0][0] = 1 
x, y = 0, 0
while N < m*n:
    nx, ny = x + dirs[n_dirs][0], y + dirs[n_dirs][1]
    if in_range(nx, ny):
        if S[nx][ny] != 0:
            n_dirs = (n_dirs + 1) % 4
        N += 1
        x, y= x + dirs[n_dirs][0], y + dirs[n_dirs][1]
        S[x][y] = N
        # print(x, y, n_dirs,S)
    else:
        n_dirs = (n_dirs + 1) % 4


for x in range(n):
    print(
        " ".join(list(map(str,S[x])))
        # S[x]
    )