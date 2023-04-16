## 반복문 정리

#### 2739번

>N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

```python
a = int(input())

for i in range(1,10):
    print(a, '*', i, '=', a*i)
```

---

#### 10950번

>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

```python
t=int(input())
#t번 만큼 a,b 받기
for i in range(t):
    a,b=map(int,input().split())
    #t번 만큼 받은 a+b출력
    print(a+b)
```
---

#### 8393번

>n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
```python
n=int(input())
#n까지 더할 변수 지정
x=0
#1 부터 n까지 반복
for i in range(1,n+1):
    #1부터 n까지 더하기
    x+=i
print(x)    
```

---

