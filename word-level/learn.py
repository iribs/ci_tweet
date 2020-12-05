#ref:
#https://machinelearningmastery.com/how-to-develop-a-word-level-neural-language-model-in-keras/


from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import Embedding
from numpy import array
import numpy as np
import textedit

in_filename = 'sequences.txt'
doc = textedit.load_doc(in_filename)
lines = doc.split('\n')

# integer encode sequences of words
tokenizer = Tokenizer(50000)
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)
vocab_size = len(tokenizer.word_index) + 1

# separate into input and output
aligned_sequneces = []
max_len = 51
for sequence in sequences:
    aligned_sequence = np.zeros(max_len, dtype=np.int64)
    aligned_sequence[:len(sequence)] = np.array(sequence, dtype=np.int64)
    aligned_sequneces.append(aligned_sequence)

sequences = np.array(aligned_sequneces)
X, y = sequences[:, :-1], sequences[:, -1]
y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]

# define model
model = Sequential()
model.add(Embedding(vocab_size, 512, input_length=seq_length))
model.add(GRU(2048, return_sequences=True))
model.add(GRU(100))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, batch_size=64, epochs=30)

# save the model to file
model.save('model.h5')
# save the tokenizer
dump(tokenizer, open('tokenizer.pkl', 'wb'))
