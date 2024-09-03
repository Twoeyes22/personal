def grow(tree):
    return [i+1 for i in tree]

N, M, X = map(int, input().split())
treeh = list(map(int, input().split()))
count = int(input())
move = input().split()
X = X - 1
result = 0

for D in move:
    # 나무꾼 위치 높이 확인
    if treeh[X] >= M:
        result += treeh[X]
        treeh[X] = 0
    
    if D == 'L':
        X = (X - 1) % N
    elif D == 'R':
        X = (X + 1) % N
    
    treeh = grow(treeh)

print(result)