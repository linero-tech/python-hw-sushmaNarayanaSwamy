from to_do import TODO


def task4():
    result = 0
    for i in range(1, 1000 + 1):
        if i % 9 == 0:
            result = result + i



    return result


if __name__ == "__main__":
    print(task4())
