print("첫째항 입력:")
a1 = int(input())
print("공차 입력:")
d = int(input())
print("항 수 입력:")
n = int(input())

print(a1, end = ' ')

sum = a1

for i in range(n-1):
    a1 += d
    sum += a1
    print(a1, end = ' ')

print()
print("합:", sum)