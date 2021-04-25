def insertion(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def bubble(arr):
    x = len(arr) - 1
    for i in range(x):
        for k in range(x-i):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                
def mergeSort(arr):
    
    if len(arr)>1:
        
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        
        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0
    
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        
        while i < len(L):
            arr[k]=L[i]
            i+=1
            k+=1
            
        while j < len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        
mylist = [3,4,5,6,23,77,-2,7,8,9,1,2]
mergeSort(mylist)
print(mylist)
        
