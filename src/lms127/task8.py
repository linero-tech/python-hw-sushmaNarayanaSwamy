from to_do import TODO


def task8(sentence, character):
    result = sentence.count(character)
    return result


if __name__ == "__main__":
    print(task8("i like music", "i"))