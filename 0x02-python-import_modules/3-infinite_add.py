#!/usr/bin/python3

if __name__ == "__main__":
    """ print the addition of all arguments """
    import sys

    count = len(sys.argv) - 1
    result = 0
    for i in range(1, count + 1):
        result += int(sys.argv[i])
    print('{}'.format(result))
