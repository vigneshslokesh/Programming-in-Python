
# def linear_search(n,x):
#     element = []

#     for i in range(1,n+1):
#         element.append(i)
#     print(element)

#     count = 0 
#     flag = 0
#     for i in element:
#         count += 1
#         if(i==x):
#             print('Yes! Number found at position: '+str(i))
#             flag = 1
#             break

#     if(flag==0):    
#         print('Number not found')
    
#     print('Number of iterations: ', str(count))

# linear_search(11150055,5955)
pos = 0
def binary_search(a,x):
    l = 0
    u = len(a)-1

    while l <= u:
        mid = (l+u) // 2

        if(a[mid] == x):
            print("Element found at: ",int(mid+1))
            return True
        else:
            if x < a[mid]:
                u = mid - 1
            else:
                l = mid + 1
    print("Element not found")
    return False

a = []
for i in range(1,11):
    a.append(i)

binary_search(a,4)