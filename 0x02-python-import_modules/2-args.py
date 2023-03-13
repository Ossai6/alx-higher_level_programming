#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    result = int(len(sys.argv)) - 1
    print("{} arguments".format(result))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
