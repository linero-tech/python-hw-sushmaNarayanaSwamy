from to_do import TODO


def task6(number):
    result = ""
    for i in str(number):
        result = i + result

    return print(int(result))


if __name__ == "__main__":
    task6(678)
    task6(432)
    task6(234)
