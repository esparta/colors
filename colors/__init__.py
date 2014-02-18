"""
ANSI colors for Python
A simple module to add ANSI colors and decorations to your strings.
"""
from __future__ import absolute_import
from .colors import color, isvalidcolor, strip_color, \
    COLORS, STYLES
from functools import partial

__all__ = ['color', 'isvalidcolor', 'strip_color', 'COLORS', 'STYLES', ]
__version__ = '1.1'

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
