## list정리

#### 10807번

>총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
```python
input()
l = list(map(int, input().split()))
n = int(input())
print(l.count(n))
```

---

#### 10871번

>정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
```python
n,x=map(int,(input().split()))
l=list(map(int,(input().split())))
# for i in range(len(l)):
#     if l[i] < x:
#         print(l[i],end=" ")

for item in l:
    if item < x:
        print(item, end=" ")
print()
```

---