l=[]
n=int(input())
for i in range(1,n+1):
    x=int(input())
    l.append(x)
print(l)
m=[]
for i in range(n):
    if l[i]>-1:
        m.append(l[i])
m=[]
for i in range(n):
    if l[i]>-1:
        m.append(l[i])
m.sort()
z=[]
for i in range(n):
    if l[i]<0:
        z.append(l[i])
z.sort()
k=[]
k=m+z
print(k)
output:
Hello World
5
1
-5
9
-6
2
[1, -5, 9, -6, 2]
[1, 9, 2, -5, -6]
