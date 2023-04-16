## 입출력, 사칙연산 정리

#### 2557번 

>Hello World!를 출력하시오.

```python
print("Hello World!")
```

---

#### 1000번

>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
```python
A,B=map(int, input().split())
print(A+B)
```

---

#### 1001번 

>두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
```python
a,b=map(int,input().split())
print(a-b)
```

---

#### 10998

>두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
```python
a,b=map(int,input().split())
print(a*b)
```

---

#### 1008번

>두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

```python
a,b=map(int,input().split())
print(a/b)
```

---

#### 10869번

>두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
```python
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
```

---

#### 10926번

>준하는 사이트에 회원가입을 하다가 joonas라는 아이디가 이미 존재하는 것을 보고 놀랐다. 준하는 놀람을 ??!로 표현한다. 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어졌을 때, 놀람을 표현하는 프로그램을 작성하시오
```python
a=input()
print(a+"??!")
```

---

#### 18108

>ICPC Bangkok Regional에 참가하기 위해 수완나품 국제공항에 막 도착한 팀 레드시프트 일행은 눈을 믿을 수 없었다. 공항의 대형 스크린에 올해가 2562년이라고 적혀 있던 것이었다.

불교 국가인 태국은 불멸기원(佛滅紀元), 즉 석가모니가 열반한 해를 기준으로 연도를 세는 불기를 사용한다. 반면, 우리나라는 서기 연도를 사용하고 있다. 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.
```python
y=int(input())
print(y-543)
```

---

#### 10430번

>(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
```python
a,b,c=map(int,input().split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
```

---

#### 2588번

>(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.



(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
```python
a=int(input())
b=int(input())
print(a*(b%10))
print(a*((b//10)%10))
print(a*(b//100))
print(a*b)
```

---

#### 11382번

>꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!
```pyton
a,b,c=map(int,input().split(" "))
print(a+b+c)
```

---