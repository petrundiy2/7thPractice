__author__ = 'Petr'
n=int(input())
A=[]
C=[]
for x in range(n):
    C=list(map(int,input().split()))
    A+=[C]
    C=[]
def Rotate(A):
    k=len(A)
    for i in range(len(A[0])-1,-1,-1):
        for j in range(len(A[0])-1,-1,-1):
            A.append(A[j][i])
    g=0
    for i in range(k,len(A)):
        A[g].append(A[i])
        if len(A[g])==2*k:
            g+=1
    A[:]=A[0:k]
    for u in range (len(A)):
        A[u]=A[u][k:len(A[u])]
    for v in range(len(A)-1,-1,-1):
        A.append(A[v])
    A[:]=A[k:len(A)]
Rotate(A)
for x in range(len(A)):
    print (' '.join(map(str, A[x])))
