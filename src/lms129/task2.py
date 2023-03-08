from to_do import TODO


def task2(number):
    result = 0

    for i in range(1, number + 1):
        if number % i == 0:
            result += 1

    return result == 2


if __name__ == "__main__":
    print(task2(7))
    print(task2(5))
    print(task2(2))
    print(task2(1))
    print(task2(10))
