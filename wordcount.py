# put your code here.
"""
for line in file
    split on spaces
        -> get back list of words
    for word in list
        populate a dictionary

"""

def count_words(path):

    file = open(path)
    word_count = {}

    for line in file:
        word_list = line.split()
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + 1

    file.close()
    return word_count
    