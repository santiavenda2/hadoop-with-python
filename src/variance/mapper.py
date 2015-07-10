#!/usr/bin/env python

import sys

print_format = "{0}{1}{2}"

mean = 0.0


def main(separator='\t'):
    for value in sys.stdin:
        value = (float(value) - mean) ** 2
        print print_format.format(value, separator, 1)

            
if __name__ == "__main__":
    main()
