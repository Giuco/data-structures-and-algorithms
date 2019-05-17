# python3

from typing import List


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.children = []

    def add_children(self, value):
        self.children.append(value)


def compute_height_naive(n: int, parents: List[int]) -> int:
    """
    >>> compute_height_naive(5, [4, -1, 4, 1, 1])
    3

    >>> compute_height_naive(5, [-1, 0, 4, 0, 3])
    4

    >>> compute_height_naive(10, [9, 7, 5, 5, 2, 9, 9, 9, 2, -1])
    4
    """
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def compute_height(n: int, parents: List[int]) -> int:
    """
    >>> compute_height(5, [4, -1, 4, 1, 1])
    3

    >>> compute_height(5, [-1, 0, 4, 0, 3])
    4

    >>> compute_height(10, [9, 7, 5, 5, 2, 9, 9, 9, 2, -1])
    4
    """
    nodes = [TreeNode(value=i) for i in range(n)]
    root = None

    for children_index in range(n):
        parent_index = parents[children_index]
        if parent_index == -1:
            root = children_index
        else:
            nodes[parent_index].add_children(nodes[children_index])

    if root is None:
        raise ValueError("Did not found the root node")

    tree_stack = [nodes[root]]
    tree_size = 0

    while tree_stack:
        tree_size += 1
        temp_tree_stack = []
        for parent in tree_stack:
            for child in parent.children:
                temp_tree_stack.append(child)
        tree_stack = temp_tree_stack

    return tree_size


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == "__main__":
    main()
