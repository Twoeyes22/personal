n = int(input())

A=map(int, input().split())
B=map(int, input().split())

Ascore=0
Bscore=0

for a,b in zip(A,B):
	if (a - b) == 7 :
		Bscore+=3
		Ascore-=1
	elif (b-a) ==7 :
		Ascore+=3
		Bscore-=1
	elif a > b:
		Ascore+=2
	elif b > a:
		Bscore+=2
	elif a == b:
		Ascore+=1
		Bscore+=1
		
print(f"{Ascore} {Bscore}")