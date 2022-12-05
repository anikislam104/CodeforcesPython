def take_input():
    s = input()
    t = input()
    return s, t


def reverse_matching(s, t):
    reversed_t = t[::-1]
    # print(reversed_t)
    print()
    if s == reversed_t:
        print("YES")
    else:
        print("NO")


def main():
    s, t = take_input()
    reverse_matching(s, t)


main()
