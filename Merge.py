def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2]

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i=0 #left array index
        j=0 #right array index
        k=0 #merged array index
        while i < len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1

            else:
                arr[k]=right_arr[j]
                j+=1
            
            k+=1

        while i < len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1

        while i < len(right_arr):
            arr[k]=right_arr[i]
            i+=1
            k+=1

test_arr = [3,8,1,0,5,7,9,2,0]
merge_sort(test_arr)
print(test_arr)