# _Array insert at index


def insertAtIndex(arr, sizeOfArray, index, element):
    if sizeOfArray == (index+1):
        arr[index] = element
    else:
        while index < sizeOfArray:
            tmp = arr[index]
            arr[index] = element
            element = tmp
            index += 1
