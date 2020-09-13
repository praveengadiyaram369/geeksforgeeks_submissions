# _Power Set Using Recursion

subset_list = []


def powerSet(s, prefix='', idx=0):

    if idx == 0:
        subset_list.clear()

    if idx == len(s):
        subset_list.append(prefix)
        return

    powerSet(s, prefix, idx+1)
    powerSet(s, prefix+s[idx], idx+1)
    return subset_list
