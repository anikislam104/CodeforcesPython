def take_input():
    year = input()
    year = int(year)
    return year


def is_all_distinct(arr):
    if len(set(arr)) == len(arr):
        print(len(set(arr)))
        print(len(arr))
        return True
    else:
        return False


def make_array_and_check(number):
    arr = []
    while number != 0:
        arr.append(number % 10)
        number = number / 10
    check = is_all_distinct(arr)
    return check


def find_next(year):
    year += 1
    while make_array_and_check(year) == False:
        year += 1
    return year


def main():
    year = take_input()
    next_such = find_next(year)
    print(next_such)


main()
