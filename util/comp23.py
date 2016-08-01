"""
python2/3 compatibility
by Hao Wu
https://github.com/Leon-Wulfgang
"""

from __future__ import print_function

if hasattr(__builtins__, 'raw_input'):
    input = raw_input
