def my_sort(x):
    even = []
    odd = []
    chars = []
    sort=dict()

    for item in x:
        if isinstance(item,int):
            if item % 2 == 0:
                even.append(item)
                
            elif item % 2 == 1:
                odd.append(item)
                
        else:
            chars.append(item)
            
    print(even)
    print(odd)
    print(chars)
    sort['even']=even
    sort['odd']=odd
    sort['chars']=chars
    print (sort)


my_sort([1, 2, 3, 4, 5, 'n', 'f'])
