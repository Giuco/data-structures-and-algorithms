# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    """
    >>> find_mismatch("[](()")
    3

    >>> find_mismatch("(())")
    'Success'

    >>> find_mismatch("{[]}()")
    'Success'

    >>> find_mismatch("{")
    1

    >>> find_mismatch("{[}")
    3

    >>> find_mismatch("foo(bar);")
    'Success'

    >>> find_mismatch("foo(bar[i);")
    10
    """
    opening_brackets_stack = []
    mismatch = None

    for i, element in enumerate(text, 1):
        if element in "([{":
            opening_brackets_stack.append(Bracket(element, i))
        elif element in ")]}":
            if len(opening_brackets_stack) == 0:
                mismatch = Bracket(element, i)
                break
            elif are_matching(opening_brackets_stack[-1].char, element):
                opening_brackets_stack.pop(-1)
            else:
                mismatch = Bracket(element, i)
                break

    if mismatch:
        result = mismatch.position
    elif opening_brackets_stack:
        result = opening_brackets_stack[-1].position
    else:
        result = "Success"

    return result


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
