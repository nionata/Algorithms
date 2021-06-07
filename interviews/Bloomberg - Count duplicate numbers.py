arr = [0, 3, 3, 3, 4, 5, 6]
target = 3

def countDuplicates(arr, target):
    def binaryLower(l, r, arr, target):
        if l > r: 
            return -1
    
        mid = l + (r - l) // 2
    
        if arr[mid] == target and (mid == 0 or arr[mid - 1] < target):
            return mid
        elif target <= arr[mid]:
            return binaryLower(l, mid - 1, arr, target)
        else:
            return binaryLower(mid + 1, r, arr, target)

    def binaryHigher(l, r, arr, target):
        if l > r: 
            return -1
    
        mid = l + (r - l) // 2
    
        if arr[mid] == target and (mid == len(arr) - 1 or arr[mid + 1] > target):
            return mid
        elif target < arr[mid]:
            return binaryHigher(l, mid - 1, arr, target)
        else:
            return binaryHigher(mid + 1, r, arr, target)
    
    lower = binaryLower(0, len(arr) - 1, arr, target)
    higher = binaryHigher(0, len(arr) - 1, arr, target)

    return higher - lower + 1
            
print(countDuplicates(arr, target))
