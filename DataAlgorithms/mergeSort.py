def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        #diving the array into 2 parts
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L)and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k] = R[j]
            j=j+1
            k=k+1


    print(arr)

mergeSort([1,2,3,4,6,1,4,10,30,12,10])

