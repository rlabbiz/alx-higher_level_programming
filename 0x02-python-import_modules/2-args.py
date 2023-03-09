#!/usr/bin/python3

if __name__ == "__main__":
    """ print the number of argrument follwed by value of it"""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print('0 arguments.')
    else:
        if count == 1:
            print('1 argument:')
        else:
            print('{} arguments:'.format(count))
        for i in range(1, count + 1):
            print('{}: {}'.format(i, sys.argv[i]))
