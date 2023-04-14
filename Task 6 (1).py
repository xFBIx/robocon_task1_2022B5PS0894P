h = [1,8,6,2,5,4,8,3,7]
#h = [1,1]
a = 0
for i in range(len(h)):
    for j in range(len(h)-1, i, -1):
        if h[i] <= h[j]:
            if (h[i] * (j-i)) > a:
                a = h[i] * (j-i)
            break
        else :
            if (h[j] * (j-i)) > a:
                a = h[j] * (j-i)
print(a)
            
