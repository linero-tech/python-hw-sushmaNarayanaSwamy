from to_do import TODO


def task9(sentence, character):
    lower_sentence = sentence.lower()
    lower_character = character.lower()
    result = lower_character in lower_sentence
    return result


if __name__ == "__main__":
    result = task9("i code in python", "i")
    print(result)
