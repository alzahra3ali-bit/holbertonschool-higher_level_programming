def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list on the same line, followed by a new line.
    Returns the actual number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")  # Prints the trailing new line
    return count
