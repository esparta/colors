# Copyright (c) 2012 Giorgos Verigakis <verigak@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""
ANSI colors for Python
A simple module to add ANSI colors and decorations to your strings.
"""
import re
from functools import partial

__version__ = '1.1'

COLORS = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
          'white')
STYLES = ('bold', 'faint', 'italic', 'underline', 'blink', 'blink2',
          'negative', 'concealed', 'crossed')


def isvalidcolor(intcolor):
    """ Is a valid color?
    Return: True if the color is an int(0,255)
    """
    return isinstance(intcolor, int) and 0 <= intcolor <= 255


def setcolor(thecolor, where="foreground"):
    """
    setcolor(thecolor, where="foreground" ) -> Return a list of the
            escape color
    [thecolor] can be a string of the COLORS tuple or an int from 0 to 255
    [where] can be only "background" or "foreground" any other value
            defaults to "foreground" values
    """

    __setup = {
        "background": (40, '48;5;'),
        "foreground": (30, '38;5;')
    }

    by_str, by_int = __setup.get(where, __setup["foreground"])
    sgr = []

    if thecolor:
        if thecolor in COLORS:
            sgr.append(str(by_str + COLORS.index(thecolor)))
        elif isvalidcolor(thecolor):
            sgr.append('{0}{1:d}'.format(by_int, thecolor))
        else:
            raise Exception('Invalid color {}'.format(thecolor))
    return sgr


def setstyle(style):
    """
    Set the style. Availible styles == STYLES. Not all styles are
    supported by all terminals.
    """
    sgr = []
    if style:
        for new_style in style.split('+'):
            if new_style in STYLES:
                sgr.append(str(1 + STYLES.index(new_style)))
            else:
                raise Exception('Invalid style "{}"'.format(new_style))
    return sgr


def color(message, foreground=None, background=None, style=None):
    """
    color function. Constructor of the basic ansi colors
    """
    sgr = []
    sgr += setcolor(foreground)
    sgr += setcolor(background, "background")
    sgr += setstyle(style)

    if sgr:
        prefix = '\x1b[' + ';'.join(sgr) + 'm'
        suffix = '\x1b[0m'
        return prefix + message + suffix
    else:
        return message


def strip_color(message):
    """ Is this used?? """
    return re.sub(r'\x1b\[.+?m', '', message)


# Foreground shortcuts
black = partial(color, foreground='black')
red = partial(color, foreground='red')
green = partial(color, foreground='green')
yellow = partial(color, foreground='yellow')
blue = partial(color, foreground='blue')
magenta = partial(color, foreground='magenta')
cyan = partial(color, foreground='cyan')
white = partial(color, foreground='white')

# Style shortcuts
bold = partial(color, style='bold')
faint = partial(color, style='faint')
italic = partial(color, style='italic')
underline = partial(color, style='underline')
blink = partial(color, style='blink')
blink2 = partial(color, style='blink2')
negative = partial(color, style='negative')
concealed = partial(color, style='concealed')
crossed = partial(color, style='crossed')
