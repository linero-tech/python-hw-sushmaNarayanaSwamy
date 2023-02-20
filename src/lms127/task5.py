from to_do import TODO


def task5(value_for_a, value_for_b):
    temp = value_for_a
    value_for_a= value_for_b
    value_for_b = temp
    print(f"a is {value_for_a}\nb is {value_for_b}")
    return value_for_a, value_for_b


if __name__ == "__main__":
    task5(4,6)
