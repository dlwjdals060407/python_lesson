import sys

a=int(input())

for i in range(a):
    a,b=map(int,(sys.stdin.readline().split()))
    print("Case #", end='')
    print(i+1, end='')
    print(':', a, '+', b, '=', a+b)