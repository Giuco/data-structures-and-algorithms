from typing import Tuple

from check_brackets import find_mismatch

N_TEST = 54


def get_test(n: int) -> Tuple[str, str]:
    with open(f"./tests/{str(n).rjust(2, '0')}") as f:
        q = f.read().strip()

    with open(f"./tests/{str(n).rjust(2, '0')}.a") as f:
        a = f.read().strip()

    return q, a


def test_check_brackets():
    for i in range(1, N_TEST + 1):
        text, correct_answer = get_test(i)

        assert correct_answer == str(find_mismatch(text)), f"{text} -> {correct_answer}"
