#first last and mid are indices, and index of key returned
#recursive
def binarySearch(arr, first, last, key):
    if last >= first:
        mid = (last+first)//2
        
        if arr[mid] == key:
            return mid
        
        elif arr[mid] > key:
            return binarySearch(arr, first, mid-1, key)
        
        else:
            return binarySearch(arr, mid+1, last, key)
    
    else:
        return -1
    
arr = [1,2,3]

print(binarySearch(arr,0,len(arr),3)==2)
