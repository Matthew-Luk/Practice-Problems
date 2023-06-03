def count_word_frequency(words):
    result = {}
    for i in words:
        result[i] = result.get(i, 0) + 1
    return result