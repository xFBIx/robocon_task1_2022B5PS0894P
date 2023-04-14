def nCr(n, r):
    return (fact(n) / (fact(r) * fact(n - r)))
 
def fact(n):
    if n == 0:
        return 1
    res = 1
    for i in range(2, n+1):
        res = res * i     
    return res

while True:
    rows = int(input("Enter the number of rows:"))
    if rows in range(1,31) :
        break
    else:
        print("Please enter the number of rows in range 1 to 30")

outer_list = []
for i in range(rows):
    inner_list = []
    for j in range(i+1):
        n = nCr(i,j)
        inner_list.append(int(n))
    outer_list.append(inner_list)

print("Elements of Pascals Triangle are: ", outer_list)
            
            

