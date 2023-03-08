from to_do import TODO


def task1(a, b):
    if a >= b:
        result = 0
    else:
        result = 0
        for i in range(a, b+1):
            result += i

    return result


if __name__ == "__main__":
    print(task1(1, 5))
    print(task1(3, 6))
    print(task1(3, 3))
