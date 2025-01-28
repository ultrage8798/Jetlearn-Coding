def binary_search(arr,low,high,key):
    mid=(low+high)//2
    if low <= high:
        if arr [mid]==key:
            return mid
        elif arr [mid]<key:
            return binary_search(arr,mid+1,high,key)
        else:
            return binary_search(arr,low,mid-1,key)
    else:
        return -1

print(binary_search([1, 2, 3, 4, 5],0,4,2))