import string


def load_doc(filename):
    text = open(filename, 'r').read()
    return text


def clean_doc(doc):
    tokens = doc.split()
    # remove punctuation
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    # make lower case
    tokens = [word.lower() for word in tokens]
    return tokens


def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()


in_filename = 'tweets.txt'
doc = load_doc(in_filename)
print(doc[:200])
tokens = clean_doc(doc)
print(tokens[:200])
print('Total Tokens: %d' % len(tokens))
print('Unique Tokens: %d' % len(set(tokens)))

# organize into sequences of tokens
length = 50 + 1
sequences = list()
for i in range(length, len(tokens)):
    seq = tokens[i - length:i]
    line = ' '.join(seq)
    sequences.append(line)
print('Total Sequences: %d' % len(sequences))

out_filename = 'sequences.txt'
save_doc(sequences, out_filename)