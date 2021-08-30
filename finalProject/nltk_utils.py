import nltk
import numpy as np
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# End goal
# 'Hi', 'How are you', 'bye', 'see you later'
# all_words = ['Hi', 'How', 'are', 'you', 'bye', 'see', 'later']
# Hi          [ 1      0       0      0     0      0        0  ]
# How are you [ 0      1       1      1     0      0        0  ]
# See you later [0      0      0      1     0      1         1 ]

def tokenize(sentence):
  # Splits string into meaningful units
  # 'do you have $1000?'
  #  ['do', 'you', 'have', '$', '1000', '?']

  # 'Is anyone there?'
  # ['Is', 'anyone', 'there', '?']
  return nltk.word_tokenize(sentence)

def stem(word):
  # Generate root of words and lower characters
  # 'organize', 'organizes', 'organizing'
  # ['organ', 'organ', 'organ']

  # ['Is', 'anyone', 'there', '?']
  # ['is', 'anyon', 'there', '?']
  return stemmer.stem(word.lower())

# Exclude punctuations
# ['is', 'anyon', 'there', '?']
# ['is', 'anyon', 'there']

def bag_of_words(tokenized_sentence, all_words):

  # sentence = ['hello', 'how', 'are', 'you']
  # words = ['hi', 'hello', 'I', 'you', 'bye', 'thank', 'cool']
  # bag =   [  0,    1,      0,    1,     0,      0,       0 ]

  tokenized_sentence = [stem(word) for word in tokenized_sentence]

  bag = np.zeros(len(all_words), dtype=np.float32)
  for index, word in enumerate(all_words):
    if word in tokenized_sentence:
      bag[index] = 1.0

  return bag


