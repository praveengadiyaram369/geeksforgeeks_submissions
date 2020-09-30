def getWater(a, b, c):
    water = min(b, c) - a
    if water > 0:
        return water
    return 0

# Complete this function


def trappingWater(arr, n):

    right = n-2
    max_right = arr[-1]
    right_arr = [max_right]
    max_left = arr[0]
    water_trapped = 0

    while right > 1:
        if arr[right] > max_right:
            max_right = arr[right]
        right_arr.append(max_right)
        right -= 1

    for idx in range(1, n-1):
        water_trapped += getWater(arr[idx], max_left, right_arr[-idx])
        if arr[idx] > max_left:
            max_left = arr[idx]

    return water_trapped
