import sys
r=int(input())

for i in range(r):
    a,b=map(int,(sys.stdin.readline().split()))
    print("Case #", end='')
    print(i+1, end='')
    print(':', a+b)