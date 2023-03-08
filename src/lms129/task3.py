from to_do import TODO


def task3(number):
    result = 1
    if number == 0:
        result = 1
    else:
        for i in range(1, number+1):
            result = result*i

    return print(result)


if __name__ == "__main__":
    task3(5)
    task3(4)
    task3(3)
    task3(8)