#! python3

dictionary = ["dog", "deer", "deal"]


def autoComplete(word):
    global dictionary
    length = len(word)
    recommendation = []
    for element in dictionary:
        if element[:length] == word:
            recommendation.append(element)
    return recommendation

print(autoComplete("de"))