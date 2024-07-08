#bubble sort
lst_us = [102, 5666, 2, 52, 98, 4, 1000]
n = 102 

def bubble(a):
    n = len(a)

    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    return a
    
print("Given List: ", lst_us)            
lst = bubble(lst_us)
print("Sorted List: ", lst)

pos = -1

def search(lst, n):
    l = 0
    u = len(lst) - 1

    while l <= u:
        mid = (l+u) // 2

        if lst[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid
            else:
                u = mid



if search(lst, n):
    print("Found at ", pos+1)

else:
    print("Not Found")