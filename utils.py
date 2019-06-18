from typing import Iterable

import pymorphy2
from pymorphy2.analyzer import Parse

from dataset import random_adjective, random_name, random_noun

parse = pymorphy2.MorphAnalyzer().parse


def inflect_to_form(dependent_word: str, main_word: str = None, tags: Iterable = None):
    if not (tags or main_word):
        raise ValueError('main_word or tags required')

    try:
        dependent_parsed: Parse = parse(dependent_word)[0]

        if main_word:
            main_tags = parse(main_word)[0].tag
            tags = set(filter(lambda v: v is not None, (main_tags.gender, main_tags.case, main_tags.number)))

        inflected = dependent_parsed.inflect(tags)
        if inflected:
            return inflected.word
        return dependent_word

    except IndexError:
        return dependent_word


def generate_chat_name():
    noun = random_noun()
    name = inflect_to_form(random_name(), tags={'gent'}).capitalize()
    adjective = inflect_to_form(random_adjective(), main_word=noun).capitalize()

    return ' '.join((adjective, noun, name))
