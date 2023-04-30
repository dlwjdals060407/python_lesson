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

#### 25304번

>준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

영수증에 적힌,

구매한 각 물건의 가격과 개수
구매한 물건들의 총 금액
을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
``` python
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
```

---

#### 25314번

>오늘은 혜아의 면접 날이다. 면접 준비를 열심히 해서 앞선 질문들을 잘 대답한 혜아는 이제 마지막으로 칠판에 직접 코딩하는 문제를 받았다. 혜아가 받은 문제는 두 수를 더하는 문제였다. C++ 책을 열심히 읽었던 혜아는 간단히 두 수를 더하는 코드를 칠판에 적었다. 코드를 본 면접관은 다음 질문을 했다. “만약, 입출력이 
$N$바이트 크기의 정수라면 프로그램을 어떻게 구현해야 할까요?”

혜아는 책에 있는 정수 자료형과 관련된 내용을 기억해 냈다. 책에는 long int는 
$4$바이트 정수까지 저장할 수 있는 정수 자료형이고 long long int는 
$8$바이트 정수까지 저장할 수 있는 정수 자료형이라고 적혀 있었다. 혜아는 이런 생각이 들었다. “int 앞에 long을 하나씩 더 붙일 때마다 
$4$바이트씩 저장할 수 있는 공간이 늘어나는 걸까? 분명 long long long int는 
$12$바이트, long long long long int는 
$16$바이트까지 저장할 수 있는 정수 자료형일 거야!” 그렇게 혜아는 당황하는 면접관의 얼굴을 뒤로한 채 칠판에 정수 자료형을 써 내려가기 시작했다.

혜아가 
$N$바이트 정수까지 저장할 수 있다고 생각해서 칠판에 쓴 정수 자료형의 이름은 무엇일까?
```python
N=int(input())

for i in range(N//4):
    print("long", end=" ")
print("int")

# while N > 0:
#     N -= 4
#     print("long", end=" ")
# print("int")
```

---

#### 15552번

>본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.

Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

자세한 설명 및 다른 언어의 경우는 이 글에 설명되어 있다.

이 블로그 글에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.
```python
import sys

a=int(input())

for i in range(a):
    m,n=map(int,(sys.stdin.readline().split()))
    print(m+n)
```

---

#### 11021번

>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
```python
import sys
r=int(input())

for i in range(r):
    a,b=map(int,(sys.stdin.readline().split()))
    print("Case #", end='')
    print(i+1, end='')
    print(':', a+b)
```

---

#### 11022번

>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
```python
import sys

a=int(input())

for i in range(a):
    a,b=map(int,(sys.stdin.readline().split()))
    print("Case #", end='')
    print(i+1, end='')
    print(':', a, '+', b, '=', a+b)
```

---

#### 2438번

>첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
```python
a=int(input())

for i in range(1,a+1):
    print('*'*i)
```

---

#### 2439번

>첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
```python
a=int(input())

for i in range(1,a+1):
    print(" "*(a-i) + "*"*i)
```

---

#### 10952번

>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
```python
while True:
    a,b=map(int,(input().split()))
    if a==0 and b==0:
        break
    print(a+b)
```

---