# _Check if array is sorted and rotated


def checkRotatedAndSorted(arr,n):
    
    cnt_up = 0
    cnt_down = 0
    
    for idx in range(1, n):
        if arr[idx] > arr[idx-1]:
            cnt_up += 1
        elif arr[idx] < arr[idx-1]:
            cnt_down += 1
    
    if (cnt_up == n-2 and cnt_down == 1 and arr[-1] < arr[0]) or (cnt_up == 1 and cnt_down == n-2 and arr[-1] > arr[0]):
        return True
    else:
        return False
