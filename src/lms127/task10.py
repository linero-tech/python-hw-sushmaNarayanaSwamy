from to_do import TODO


def task10_1(assessments):
    result1 = len(assessments)
    return result1

def task10_2(assessments):
    result2 = assessments[3]
    return result2

def task10_3(assessments):
   return assessments[len(assessments) // 2]
def task10_4(assessments):
    result = assessments[0:3]
    return result


if __name__ == "__main__":
    print(task10_1("ABCDE"))
    print(task10_2("ABCDE"))
    print(task10_3("ABCDE"))
    print(task10_4("ABCDE"))
