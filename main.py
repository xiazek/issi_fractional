from fractional import Fractional

if __name__ == '__main__':
    f1 = Fractional(1, 2)  # 1/2
    f2 = Fractional(1, 3)  # 1/3

    sum_result = f1 + f2
    print(f"{f1} + {f2} = {sum_result}")

    sub_result = f1 - f2
    print(f"{f1} - {f2} = {sub_result}")

    mul_result = f1 * f2
    print(f"{f1} * {f2} = {mul_result}")

    div_result = f1 / f2
    print(f"{f1} / {f2} = {div_result}")

    # Operations with integers
    print(f"{f1} + 1 = {f1 + 1}")
    print(f"1 + {f1} = {1 + f1}")
    print(f"{f1} - 1 = {f1 - 1}")
    print(f"1 - {f1} = {1 - f1}")
    print(f"{f1} * 2 = {f1 * 2}")
    print(f"2 * {f1} = {2 * f1}")
    print(f"{f1} / 2 = {f1 / 2}")
    print(f"2 / {f1} = {2 / f1}")

    # Comparisons
    print(f"{f1} == {f2}: {f1 == f2}")
    print(f"{f1} < {f2}: {f1 < f2}")
    print(f"{f1} > {f2}: {f1 > f2}")
    print(f"{f1} == 0.5: {f1 == Fractional(1,2)}")
    print(f"{f1} > 0: {f1 > 0}")
    print(f"{f1} < 1: {f1 < 1}")
