def take_input():
    n, h = input().split()
    n = int(n)
    # h = input()
    h = int(h)
    heights = input().split()
    for i in range(n):
        heights[i] = int(heights[i])
    return n, h, heights


def calculate_width(n, h, heights):
    width = 0
    for i in range(n):
        if heights[i] > h:
            width += 2
        else:
            width += 1
    return width


def main():
    n, h, heights = take_input()
    width = calculate_width(n, h, heights)
    print(width)


main()
