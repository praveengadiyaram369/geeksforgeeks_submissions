# _String Permutations

subset_list = []


def replace_char(s, begin, end):
    s_list = list(s)
    A = s_list[begin]
    B = s[end]
    s_list[begin], s_list[end] = B, A
    return ''.join(s_list)


def perform_perm(S, idx=0):
    if idx == 0:
        subset_list.clear()

    if idx == len(S):
        if S not in subset_list:
            subset_list.append(S)
        return

    for i in range(len(S)):
        perform_perm(replace_char(S, idx, i), idx+1)

    return subset_list

# Complete this function


def permutation(S):
    result = perform_perm(S)
    print(' '.join(sorted(result)), end='')
