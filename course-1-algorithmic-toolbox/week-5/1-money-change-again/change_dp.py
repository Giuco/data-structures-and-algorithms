# Uses python3
import sys


def get_change(m):
    # write your code here
    return m // 4


if __name__ == '__main__':
    m_input = int(sys.stdin.read())
    print(get_change(m_input))
