a1=int(input())
r=int(input())
n=abs(int(input()))

def PA(a1, r, n):
    an = int(a1 + (n-1)*r)
    S = int((n*(a1+an))/2)
    return S
print(PA(a1,r,n))