"""
Sampling the testing module
"""

#!/usr/bin/env python

from __future__ import print_function

from colors import color, COLORS, STYLES


for background in (None,) + COLORS:
    for foreground in (None,) + COLORS:
        for style in (None,) + STYLES:
            text = ('%s' % (foreground or 'normal')).ljust(7)
            print(color(text, foreground=foreground,
                        background=background, style=style), end=' ')
        print()

for i in range(256):
    if i % 64 == 0:
        print()
    print(color(' ', background=i), end='')

print()
