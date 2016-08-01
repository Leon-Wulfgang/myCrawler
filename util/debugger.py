"""
utils.debugger
by Hao Wu
https://github.com/Leon-Wulfgang
"""


def peek(*p):
    """
    peek a var
    :param p: pointer to the variable to be peeked
    :return: void
    """
    for var in p:
        print var
        print type(var)

