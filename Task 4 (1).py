c = input('Enter the moves:')
c = c.replace(' ','')
c = c.lower()
y = 0
x = 0
t = 0
for i in c:
    if i == 'u':
        y += 1
    elif i == 'd':
        y -= 1
    elif i == 'r':
        x += 1
    elif i == 'l':
        x -= 1
    else:
        print('Please enter a valid move.')
        t = 1
        break
if y == 0 and x == 0 and t == 0:
    print('true')
elif t == 0:
    print('false')
