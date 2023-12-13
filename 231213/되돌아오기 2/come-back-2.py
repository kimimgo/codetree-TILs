#  북쪽을 향한 상태에서 움직이는 것을 시작
#   N개의 명령

#   F, L, R
# 1초에 한칸 / 회전에도 1초의 시간이 걸린다 

# 몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단하는 프로그램을 작성해보세요.

# 1 ≤ 명령의 길이 ≤ 100,000

mapper = {
    # x, y
    0: [0, 1],
    1: [1, 0],
    2: [0, -1],
    3: [-1, 0],
}

def solution():
    x, y, idir, sec = 0, 0, 0, 0
    for dir in input():
        if dir == 'L':
            idir = abs((idir - 1 )% 4)
            sec += 1
            continue
        elif dir == 'R':
            idir = (idir + 1 )% 4
            sec += 1
            continue

        dpos = mapper[idir]
        _x, _y = x, y
        x, y = x + dpos[0], y + dpos[1]
        sec += 1
        if _x * x < 0 and y == 0:
            return (sec)
        elif _y * y < 0 and x == 0:
            return (sec)
        elif x == y == 0:
            return (sec)
    return (-1)

print(solution())