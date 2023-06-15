import random


def generate_random_code(number_of_digits):
    """
    Generates a random string code containing the numbers 0-9.
    """

    choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    return "".join(random.choices(choices, k=number_of_digits))
