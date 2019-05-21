from typing import Tuple, List

from process_packages import Request, process_buffer

N_TEST = 22


def get_test(n: int) -> Tuple[int, Request, List[int]]:
    with open(f"./tests/{str(n).rjust(2, '0')}") as f:
        q = f.read().strip().split("\n", 1)

    buffer_size = int(q[0].split()[0])

    if len(q) > 1:
        data = q[1]
        data = list(map(lambda x: list(map(int, x.split())), data.split("\n")))
        data = list(map(lambda x: Request(*x), data))
    else:
        data = []

    with open(f"./tests/{str(n).rjust(2, '0')}.a") as f:
        answer = list(map(int, f.read().split()))

    return buffer_size, data, answer


def test_check_brackets():
    for i in range(1, N_TEST + 1):
        buffer_size, messages, correct_answer = get_test(i)
        answer = list(map(lambda x: x.started_at, process_buffer(buffer_size, messages)))

        assert correct_answer == answer, i
