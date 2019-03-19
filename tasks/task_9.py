import math


def find_abc():
    i = 1000
    find = None
    for a in range(1, int(i/2)):
        for b in range(1, int(i/2)):
            c = math.sqrt((a**2) + (b**2))
            if c+a+b == i:
                find = [a, b, c]
                break
        if find:
            break
    return find


if __name__ == '__main__':
    print(find_abc())
