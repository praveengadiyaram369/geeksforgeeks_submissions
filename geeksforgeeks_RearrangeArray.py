# _Rearrange an array with O(1) extra space


def arrange(arr, n):

    for idx in range(n):
        arr[idx] += (arr[arr[idx]] % n)*n

    for idx in range(n):
        arr[idx] = int(arr[idx]/n)
