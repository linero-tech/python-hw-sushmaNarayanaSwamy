from to_do import TODO


def task6(number):
    result = ""
    for i in str(number):
        result = i + result

    return int(result)


if __name__ == "__main__":
    print(task6(678))
    print(task6(432))
    print(task6(234))
