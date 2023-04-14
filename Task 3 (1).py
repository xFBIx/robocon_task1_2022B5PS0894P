st = input('Enter a string of parantheses:')
newst= st.replace(' ','')
if len(newst)%2 != 0:
    print('false')
else:
    i_list = []
    o_list = []
    source_list = [['(',')'],['[',']'],['{','}']]
    for i in range(len(newst)):
        if len(i_list) < 2 :
            i_list.append(newst[i])
            if len(i_list) == 2:
                o_list.append(i_list)
                i_list = []
    for j in o_list:
        t = 1
        if j not in source_list:
            t = 0
            break
    if t == 0:
        print('false')
    else:
        print('true')

       
