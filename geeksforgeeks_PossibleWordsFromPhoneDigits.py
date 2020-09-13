# _Possible Words From Phone Digits

phone_digit_dict = {2: 'abc', 3: 'def', 4: 'ghi',
                    5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
subset_list = []

# Complete this function


def possibleWords(a, N, prefix='', idx=0):

    if idx == 0:
        subset_list.clear()

    if idx == N:
        subset_list.append(prefix)
        return

    for char in phone_digit_dict[a[idx]]:
        possibleWords(a, N, prefix+char, idx+1)

    return subset_list
