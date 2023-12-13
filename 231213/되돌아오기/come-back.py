N = int(input())    # N번에 걸쳐 움직이려는 방향과 움직일 거리

mapper = {
    # x, y
    'W': [-1, 0],
    'S': [0, -1],
    'N': [0, 1],
    'E': [1, 0],
}

# 1초에 한 칸씩 움직인다고 했을 때, 
# 몇 초? 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단
# W, S, N, E중에 하나이며 각각 서, 남, 북, 동쪽으로 이동함을 의미합니다.

def solution(N):
    pos = [0, 0]
    sec = 0
    # for d, k in zip(["N","S"],[3,3]):
    for _ in range(N):
        d, k = input().split()
        k = int(k)
        sec += k
        dpos = list(map(lambda x: x*k, mapper[d]))
        _pos = pos
        pos = [p+dp for p, dp in zip(pos, dpos)]
        # print(_pos,pos, sec)
        if pos == [0,0]:
            return sec
        elif pos[0] * _pos[0] < 0:
            return (sec-abs(pos[0]))
        elif pos[1] * _pos[1] < 0:
            return (sec-abs(pos[1]))

    return -1

print(solution(N))

# if pos[0] == 0 and pos[1] == 0:
#     print(sum(pos))
# else:
#     print(-1)