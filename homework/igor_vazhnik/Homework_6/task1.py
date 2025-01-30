text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
# print(text)
words = text.split()
# print(words)
fin_words = []
for word in words:
    if ',' in word:
        word = word.replace(',', 'ing')
        word = word + ','
        fin_words.append(word)
    elif '.' in word:
        word = word.replace('.', 'ing')
        word = word + '.'
        fin_words.append(word)
    else:
        word = word + 'ing'
        fin_words.append(word)
print(' '.join(fin_words))
