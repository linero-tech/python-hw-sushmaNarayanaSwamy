from to_do import TODO


def task5(sentence):
    result = 0
    for i in range(len(sentence)):
        result += 1
    return result


if __name__ == "__main__":
    print(task5("I love GBG"))
