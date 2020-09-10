# _Tower Of Hanoi


def toh(N, fromm, to, aux):

    print_fmt = "move disk {} from rod {} to rod {}"

    if N == 1:
        print(print_fmt.format(N, fromm, to))

        return 1

    step_cnt = 0

    step_cnt += toh(N-1, fromm, aux, to)
    step_cnt += 1
    print(print_fmt.format(N, fromm, to))
    step_cnt += toh(N-1, aux, to, fromm)

    return step_cnt
