#! python3

dictionary = {"the": True,
              "quick": True,
              "brown": True,
              "fox": True,
              "bed": True,
              "bath": True,
              "bedbath": True,
              "beyond": True,
              "and": True}

sentences = ["thequickbrownfox", "bedbathandbeyond"]


def splitter(sentence):
    global dictionary
    sent_list = []
    ptr = 0
    word = []
    while ptr < len(sentence):
        word.append(sentence[ptr])
        try:
            if dictionary[''.join(word)]:
                sent_list.append(''.join(word))
                word = []
        except:
            pass
        ptr += 1
    return sent_list


for sentence in sentences:
    print(splitter(sentence))
