#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count_result = len(argv) - 1
    if count_result == 0:
        print("0 arguments.")
    elif count_result == 1:
        print("1 arguments:")
    else:
        print("{} arguments".format(count_result))
    for i in range(count_result):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
