n,x=map(int,(input().split()))
l=list(map(int,(input().split())))
# for i in range(len(l)):
#     if l[i] < x:
#         print(l[i],end=" ")

for item in l:
    if item < x:
        print(item, end=" ")
print()