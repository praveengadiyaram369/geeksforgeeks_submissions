# _Max and Second Max

def largestAndSecondLargest(sizeOfArray, arr):
    
    li = [-1, -1]
    for val in arr:
        if val > li[0]:
            if li[0] != -1:
                li[1] = li[0]
                
            li[0] = val
        elif val > li[1] and val != li[0]:
            li[1] = val
            
    return li