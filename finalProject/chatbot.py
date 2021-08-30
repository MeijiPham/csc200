import random
import json
import torch
from model import NeuralNetwork
from nltk_utils import bag_of_words, tokenize

# Use NLP to tokenize, stem, and create an array with the types of word used
# After array is finished, it becomes the training data
# Feed training data into neural network model (two-layer in this case) using pytorch framework
# Load the model and implement the chat


device = torch.device('cpu')

with open('intents.json', 'r') as fhand:
  intents = json.load(fhand)

file = 'data.pth'
data = torch.load(file)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']


model = NeuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

possible_exit = ['Goodbye', 'Bye']
bot_name = 'Apollo'
user_name = input('Please enter your name: ')
print(f'Hi {user_name[0].upper() + user_name[1:]}! I\'m Apollo, your personal therapy bot!')
print('If you have anything you wish to talk about, please share them with me. Don\'t be afraid to speak your mind!')
print('If you wish to leave, then say, \'Goodbye\'.')

while True:
  sentence = input('You: ')
  if sentence[0].upper() + sentence[1:] in possible_exit:
    print(f'{bot_name}: Thank you for chatting with me! I hope things will look brighter in your future!')
    break

  sentence = tokenize(sentence)
  x = bag_of_words(sentence, all_words)
  x = x.reshape(1, x.shape[0])
  x = torch.from_numpy(x).to(device)

  output = model(x)
  _, predicted = torch.max(output, dim=1)
  tag = tags[predicted.item()]

  probability = torch.softmax(output, dim=1)
  prob = probability[0][predicted.item()]

  if prob.item() > 0.75:
    for intent in intents['intents']:
      if tag == intent['tag']:
        print(f"{bot_name}: {random.choice(intent['responses'])}")
  else:
    print(f'{bot_name}: I\'m sorry. I do not comprehend.')
