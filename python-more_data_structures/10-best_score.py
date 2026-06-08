#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_key = list(a_dictionary.keys())[0]
    for key, value in a_dictionary.items():
        if value > a_dictionary[max_key]:
            max_key = key

    return max_key
