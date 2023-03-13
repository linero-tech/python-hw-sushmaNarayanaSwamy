from to_do import TODO


def task9(temperature):
    t1 = len(temperature) - 1
    temp = int(temperature[:t1])
    unit = (temperature[t1:]).lower()
    if unit == "f":
        result = str(int((temp - 32) * 5 / 9)) + "c"

    elif unit == "c":
        result = str(int((temp * 9 / 5) + 32)) + "F"

    print(result)
    return result


if __name__ == "__main__":
    task9("-30C")
    task9("-20C")
    task9("50f")
