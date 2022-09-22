def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    for i in range(len(numbers)):
        x = max(numbers(i))
    return x


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
