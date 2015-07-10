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
                print "{0}{1}{2}".format(word, separator, file_name+':'+str(line_number))

if __name__ == "__main__":
    main()
