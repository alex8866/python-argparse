#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description = 'Change the option prefix characters.', prefix_chars = '-+/')

parser.add_argument('-a', action = 'store_false', default = None, help = 'Turn off')
parser.add_argument('+a', action = 'store_true', default = None, help = 'Turn on')
parser.add_argument('//noarg', '++noarg', action = 'store_true', default = False)

print parser.parse_args()
