s = int(input('Enter the web page area: '))
lst = []
for i in range(1,s//2+1):
    if s%i == 0:
        ls = []
        l = s/i
        ls.append(int(l))
        ls.append(i)
        if l >= i:
            lst.append(ls)
t = lst[0][0] - lst[0][1]
for i in range(len(lst)):
    d = lst[i][0] - lst[i][1]
    if d < t:
        t = d
        a = lst[i]
print(a)
        
