
def search (T = "My Name is Bada",  P = 'ada'):
    n=len(T)
    m=len(P)
    print(n,m)
    for i in range(0,  n-m+1):
    # print(T[i])
        j=0
        while(j<m and P[j]==T[i+j]):
            j=j+1
        if m==j:
            # print(T[i], T[i+2])
            return T[i:i+m]
    return ""

a= search("I am Badar Saghir", "Badar Saghir");
print(a)



