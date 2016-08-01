"""
AnyAnt
A web crawler project dedicated to provide customizable web scrapping service to anyone.
by Hao Wu
https://github.com/Leon-Wulfgang
"""
import sys
from model import queen


def main():
    print("Welcome to AnyAnt")
    q = queen.Queen(sys.argv)
    q.work()


"""
entrance
"""
if __name__ == "__main__":
    main()
