# _Who has the majority?


def majorityWins(arr, n,  x, y):

    x_cnt = y_cnt = 0
    for val in arr:
        if val == x:
            x_cnt += 1
        elif val == y:
            y_cnt += 1

    if x_cnt > y_cnt:
        return x
    elif y_cnt > x_cnt:
        return y
    else:
        return min(x, y)
