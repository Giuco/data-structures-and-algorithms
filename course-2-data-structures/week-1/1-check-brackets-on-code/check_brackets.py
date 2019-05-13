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

    for i, element in enumerate(text):
        if element in "([{":
            opening_brackets_stack.append(Bracket(element, i))
        elif element in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            elif any([element == ")" and opening_brackets_stack[-1][0] == "(",
                      element == "]" and opening_brackets_stack[-1][0] == "[",
                      element == "}" and opening_brackets_stack[-1][0] == "{"]):
                opening_brackets_stack.pop(-1)
            else:
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[-1][1] + 1

    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
