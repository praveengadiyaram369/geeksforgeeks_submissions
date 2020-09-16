# _Exactly 3 Divisors

def exactly3Divisors(N):
    N_sqrt = math.floor(math.sqrt(N))
    N_sqrt += 1
    divisors_list = [0] * (N_sqrt)
    divisors_count = 0
    for i in range(N_sqrt):
        if i > 1 and divisors_list[i] == 0:
            #print(i)
            divisors_count += 1
            j = 2 * i
            while j < N_sqrt:
                divisors_list[j] = 1
                j += i
    return divisors_count