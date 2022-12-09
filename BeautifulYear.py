def take_input():
    year = input()
    year = int(year)
    return year


def is_all_distinct(arr):
    if len(set(arr)) == len(arr):
        return True
    else:
        return False


def make_array_and_check(number):
    arr = []
    while number != 0:
        arr.append(number % 10)
        number = int(number / 10)
        # print(number)
    check = is_all_distinct(arr)
    return check


def find_next(year):
    year += 1
    while not make_array_and_check(year):
        year += 1
    return year


def main():
    year = take_input()
    next_such = find_next(year)
    print(next_such)


main()
