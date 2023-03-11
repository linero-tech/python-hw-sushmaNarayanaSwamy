from to_do import TODO


def task3(number):
    result = 1

    for i in range(1, number+1):
        result = result*i

    return result


if __name__ == "__main__":
    print(task3(0))
    print(task3(4))
    print(task3(3))
    print(task3(5))