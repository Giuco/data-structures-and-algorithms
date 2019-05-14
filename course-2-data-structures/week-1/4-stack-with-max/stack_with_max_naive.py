# python3
import sys
from typing import List, Optional, Tuple


class StackWithMaxNaive:
    def __init__(self):
        self.__stack = []

    def __len__(self):
        return len(self.__stack)

    def push(self, a):
        self.__stack.append(a)

    def pop(self):
        self.__stack.pop()

    def max(self):
        return max(self.__stack)


class StackWithMaxEfficient:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, a):
        self.stack.append(a)

        if len(self.max_stack) == 0:
            self.max_stack.append(a)
        elif a > self.max_stack[-1]:
            self.max_stack.append(a)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.stack.pop()
        self.max_stack.pop()

    def max(self):
        return self.max_stack[-1]


def interpret_input(queries: List[Tuple[str, Optional[int]]]):
    """
    >>> interpret_input([("push", 2), ("push", 1), ("max", ), ("pop", ), ("max", )] )
    [2, 2]

    >>> interpret_input([("push", 1), ("push", 2), ("max", ), ("pop", ), ("max", )] )
    [2, 1]

    >>> interpret_input([("push", 2), ("push", 3), ("push", 9), ("push", 7), ("push", 2), ("max", ), ("max", ), ("max", ), ("pop", ), ("max", )])
    [9, 9, 9, 9]

    >>> interpret_input([("push", 7), ("push", 1), ("push", 7), ("max", ), ("pop", ), ("max", )])
    [7, 7]

    >>> interpret_input([("push", 1), ("push", 7), ("pop", )])
    []
    """
    stack = StackWithMaxEfficient()
    lengths = []

    for query in queries:
        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            lengths.append(stack.max())

    return lengths


def main():
    num_queries = int(sys.stdin.readline())
    queries_input = list()

    for _ in range(num_queries):
        queries_input.append(sys.stdin.readline().split())

    output_lengths = interpret_input(queries_input)
    print("\n".join(map(str, output_lengths)))


if __name__ == "__main__":
    main()
