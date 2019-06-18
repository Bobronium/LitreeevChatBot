import random
from itertools import islice

ADJECTIVES_FILE = 'dataset/adjectives.txt'
NOUNS_FILE = 'dataset/nouns.txt'
NAMES_FILE = 'dataset/names.txt'

with open(ADJECTIVES_FILE, 'r') as adjectives:
    ADJECTIVES_COUNT = len([0 for adj in adjectives])

with open(NOUNS_FILE, 'r') as nouns:
    NOUNS_COUNT = len([0 for noun in nouns])

with open(NAMES_FILE, 'r') as names:
    NAMES_COUNT = len([0 for name in names])


def get_random_line(filename, file_length):
    with open(filename, 'r') as file:

        random_line = random.randint(0, file_length)
        for _ in islice(file, random_line - 1):
            pass  # skip n-1 lines

        return file.readline().strip()


def random_adjective():
    return get_random_line(ADJECTIVES_FILE, ADJECTIVES_COUNT)


def random_noun():
    return get_random_line(NOUNS_FILE, NOUNS_COUNT)


def random_name():
    return get_random_line(NAMES_FILE, NAMES_COUNT)
