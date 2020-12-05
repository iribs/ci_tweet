import random
from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import textedit


def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
    result = list()
    in_text = seed_text
    # generate a fixed number of words
    for _ in range(n_words):
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        # predict probabilities for each word
        yhat = model.predict_classes(encoded, verbose=0)
        # map predicted word index to word
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        in_text += ' ' + out_word
        result.append(out_word)
    return ' '.join(result)


in_filename = 'sequences.txt'
doc = textedit.load_doc(in_filename)
lines = doc.split('\n')
seq_length = len(lines[0].split()) - 1

model = load_model('model.h5')
tokenizer = load(open('tokenizer.pkl', 'rb'))

seed_text = 'computer'
print(seed_text, ":\n")
generated = generate_seq(model, tokenizer, seq_length, seed_text, random.randint(0, 50))
print(generated)