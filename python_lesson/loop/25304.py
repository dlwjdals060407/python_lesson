#금액
X=int(input())
#물건 종류수
N=int(input())
sum=0
#N줄 만큼 a,b주어짐
for i in range(N):
    a,b=map(int,(input().split()))
    sum+=a*b

if X==sum:
    print("Yes")
else:
    print("No")

