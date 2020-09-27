

def rearrange(arr, n):

    right = n-1
    left = 0
    rem = arr[-1]+1

    for idx in range(n):
        if idx % 2 == 0:
            arr[idx] += (arr[right] % rem) * rem
            right -= 1
        else:
            arr[idx] += (arr[left] % rem) * rem
            left += 1

    for idx in range(n):
        arr[idx] = int(arr[idx]/rem)
