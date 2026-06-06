#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Initialize the sum variable
    total_sum = 0

    # Slice sys.argv from index 1 onward to grab only the passed arguments
    for arg in sys.argv[1:]:
        total_sum += int(arg)

    # Print the final result followed by a newline
    print("{}".format(total_sum))
