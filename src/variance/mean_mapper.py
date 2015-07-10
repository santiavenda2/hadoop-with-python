#!/usr/bin/env python

import sys

print_format = "{0}{1}{2}"


def main(separator='\t'):
    for value in sys.stdin:
        value = float(value)
        print print_format.format(value, separator, 1)

if __name__ == "__main__":
    main()
