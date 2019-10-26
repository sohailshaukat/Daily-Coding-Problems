#! python3

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

line = []
lines = []
for word in words:
    if len(' '.join(line))+len(word) < 16:
        line.append(word)
    else:
        lines.append(line)
        line = [word]
if line != []:
    lines.append(line)

sentence = []
sentences = []

for ptr, line in enumerate(lines):
    if len(line) == 1:
        sentence = line[0].rjust(k, " ")
    else:
        spaces_count = len(line) - 1
        spaces = k - len(''.join(line))
        space_len = spaces//spaces_count
        space = " "*space_len
        if len(space.join(line)) != k:
            additional_spaces = k - len(space.join(line))
            line[-1] = " "*additional_spaces+line[-1]
        sentence = space.join(line)
    sentences.append(sentence)

print(*sentences, sep='\n')
