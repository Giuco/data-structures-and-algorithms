from max_pairwise_product import max_pairwise_product_original, max_pairwise_product
from random import randint


def stress_test():
    for _ in range(1000):

        input_n = randint(2, 1000)
        input_numbers = [randint(1, 10000) for _ in range(input_n)]

        original_result = max_pairwise_product_original(input_numbers)
        my_result = max_pairwise_product(input_numbers)

        input_numbers = [str(x) for x in input_numbers]

        print("Input numbers: {}".format(' '.join(input_numbers)))
        print("My Result: {} \t Original Result: {}".format(my_result, original_result))

        if original_result != my_result:
            break


if __name__ == '__main__':
    stress_test()
