D = {}

D['R'] = [0 , 1] # 
D['L'] = [0 , -1] # 
D['U'] = [-1, 0] # 
D['D'] = [1, 0] # 

# n t
# r c d
# 26 41
# 8 3 D
# n, t = tuple(map(int,input().split()))
# x, y, d = tuple(input().split())
# x, y = int(x), int(y)

n, t = 26, 41
x, y, d = 8, 3, 'D'

def in_range(x, y):
    return x > 0 and y > 0 and x <= n and y <= n

ds = D[d]
_t = 0
# print(x, y, _t)
while t > _t:
    nx, ny = x + ds[0], y + ds[1]
    if not in_range(nx, ny):
        ds = list(map(lambda x: x*-1, ds))
        _t += 1
        # print(x, y, _t)
        continue
    x, y = x + ds[0], y + ds[1]
    _t += 1
    # print(x, y, _t)

print(x, y)