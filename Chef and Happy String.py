T=int(input())
for i in range (0,T):
    input_str_array = list(input())
    #print(input_str_array)
    s=len(input_str_array)
    #print(s)
    s1=0
    ss1=0
    ss2=0
    for j in range(0,s):
        if j<s-2:
            if (input_str_array[j].lower() in ('a', 'e', 'i', 'o', 'u')):
                if(input_str_array[j+1].lower() in ('a', 'e', 'i', 'o', 'u')):
                    if(input_str_array[j+2].lower() in ('a', 'e', 'i', 'o', 'u')):
                        s=3
                    
    if s==3:
        print('Happy')
        
    else:
         print('Sad')
