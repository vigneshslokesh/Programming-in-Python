
def linear_search(n,x):
    element = []

    for i in range(1,n+1):
        element.append(i)
    print(element)

    count = 0 
    flag = 0
    for i in element:
        count += 1
        if(i==x):
            print('Yes! Number found at position: '+str(i))
            flag = 1
            break

    if(flag==0):    
        print('Number not found')
    
    print('Number of iterations: ', str(count))

    

linear_search(11150055,5955)