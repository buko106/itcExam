def S( n, m ):
    if n > m > 0:
        return S(n-1,m-1) + (n-1)*S(n-1,m)
    elif n == m and m>=0:
        return 1
    else:
        return 0
    
def q( n, m ):
    ans = S(n,m)
    for i in range(1,n+1):
        ans /= i
        
    return ans

print(q(3,2))
print(1/2)
print()
print(q(3,3))
print(1/6)
print()
print(q(4,3))
print(6/24)
print()
for n in range(4,10):
    print(q(n,1))
    print(1/n)
    print()
