#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Get the list of arguments excluding the script name
    args = sys.argv[1:]
    count = len(args)

    # Determine the correct punctuation and pluralization
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Print each argument with its 1-indexed position
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
