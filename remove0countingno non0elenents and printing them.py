l=[]
n=int(input())
for i in range(1,n+1):
    x=int(input())
    l.append(x)
print(l)
m=[]
c=0
for i in range(n):
    if l[i]!=0:
        c=c+1
        m.append(l[i])
print(" non-zero elements=",m)
print("count=",c)
output:
  5
2
0
4
0
23
[2, 0, 4, 0, 23]
 non-zero elements= [2, 4, 23]
count= 3
