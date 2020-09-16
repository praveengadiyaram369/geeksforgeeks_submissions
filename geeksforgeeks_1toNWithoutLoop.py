# _Print 1 To N Without Loop


def printNos(N):
    if N < 2:
        print(str(N), end=" ")
    else:
        printNos(N-1)
        print(str(N), end=" ")
