N, M, X = map(int, input().split())
treeh = list(map(int, input().split()))
count = int(input())
move = input().split()
X -= 1
result = 0

for i in range(count):
    # 나무꾼 위치 높이 확인
    if treeh[X] + i >= M:
        result += treeh[X] + i
        treeh[X] -= treeh[X] + i
         
    
    if move[i] == 'L':
        X = (X - 1 +N) % N
    elif move[i] == 'R':
        X = (X + 1) % N
    
print(result)