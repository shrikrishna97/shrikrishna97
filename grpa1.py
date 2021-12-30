def sub(L):
    ls = [[]]
    L.sort()
    for i in range(len(L)+1):
        for j in range(i):
            ls.append(L[j:i])
    return (ls)      

# print(sub(L))

def find_Min_Difference(L,P):
    li = []
    
    min = 100000
    for i in sub(L):
        if len(i) == P:
            li.append(i)
    
    for i in li:
        d =i[-1] - i[0]
        if (d)< min:
            min = d
    return min        

L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))
