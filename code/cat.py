#!/usr/bin/env python

# Displays the contents of a text file to terminal, like unix 'cat' command

import sys

# TODO verify args, print usage

filename = sys.argv[1]

with open(filename, 'r') as input:
    for line in input:
        sys.stderr.write(line)
