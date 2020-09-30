# _Stock buy and sell


def stockBuySell(A, n):

    stocks = []
    low = None

    for idx in range(1, n):
        if low is None and A[idx] > A[idx-1]:
            low = A[idx-1]
            stocks.append(idx-1)
        elif low is not None and A[idx] < A[idx-1] and A[idx-1] > low:
            stocks.append(idx-1)
            low = None

    if low is not None and A[-1] > low:
        stocks.append(n-1)
    elif low is not None and A[-1] <= low:
        stocks.pop()

    if len(stocks) > 0:
        result = ''
        for idx in range(0, len(stocks), 2):
            result += '('+str(stocks[idx])+' '+str(stocks[idx+1])+') '
        print(result)
    else:
        print('No Profit')
