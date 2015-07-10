#!/usr/bin/env python

import sys
import os

# file_name = os.environ["map_input_file"]
file_path, file_name = os.path.split(os.getenv("map_input_file"))


def main(separator='\t'):
    for line_number, line in enumerate(sys.stdin):
        for word in line.split():
            word = word.strip('!?"-.,_ \'()[]').lower()
            if word.isalpha():
                print "{0}{1}{2}{1}{3}".format(word, separator, line_number, file_name)

if __name__ == "__main__":
    main()
