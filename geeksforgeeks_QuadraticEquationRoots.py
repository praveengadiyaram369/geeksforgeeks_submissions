# _Quadratic Equation Roots


def quadraticRoots(a, b, c):
    det = (b * b) - (4 * a * c)
    if det < 0:
        print("Imaginary")
    elif det == 0:
        root = math.floor(-b/(2.0 * a))
        print(str(root) + " " + str(root))
    else:
        root_1 = math.floor((-b + math.sqrt(det))/(2.0 * a))
        root_2 = math.floor((-b - math.sqrt(det))/(2.0 * a))
        print(str(root_1) + " " + str(root_2))
