# _Digits In Factorial


def digitsInFactorial(N):
    log_sum = 0
    for i in range(N+1):
        if i > 0:
            log_sum += math.log(i, 10)

    return math.ceil(log_sum)
