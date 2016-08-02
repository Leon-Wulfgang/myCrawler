"""
AnyAnt
A web crawler project for providing customizable web scrapping service.
by Hao Wu
https://github.com/Leon-Wulfgang
"""
import sys
from model import queen


def main():
    # greets the user
    print("Welcome to AnyAnt")

    # start a queen instance to manage workers
    # sys.argv passed to queen including
    #   service_name: the name of the service to run
    q = queen.Queen(sys.argv)

    # queen start to work on workers
    q.work()

# entrance
if __name__ == "__main__":
    main()
