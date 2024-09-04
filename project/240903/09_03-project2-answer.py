import sys
input = sys.stdin.readline

N, M, x = map(int, input().split())
x -= 1
H = list(map(int, input().split()))
Q = int(input())
D = input().rstrip().split()

ans = 0

for i in range(Q):
	# 1. 벌목할 수 있으면 벌목
	if H[x] + i >= M:  # 나무의 높이는 i만큼 자랐다.
			ans += H[x] + i
			H[x] -= H[x] + i

	# 2. 움직이기
	if D[i] == 'L':
		x = (x - 1 + N) % N
	elif D[i] == 'R':
		x = (x + 1) % N

print(ans)