import string
import random


def get_random_name():
    return "".join(random.choices(string.ascii_letters, k=len(string.ascii_letters)))