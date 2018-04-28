
# coding: utf-8

# In[1]:


# Training model

import nltk
from nltk.stem.lancaster import LancasterStemmer
from pyvi import ViTokenizer

stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random


# In[2]:


# data json
# {   "tag": "menu",
#         "patterns": ["I want to order", "What kinds of food are there?", "What is your delicous food?" ],
#         "responses": ["Are you ready to order? Our restaurant have pizza, vegetable pasta, beefsteack. These is special of our restaurant", "Can I help you? This is menu. Please ask me if you have any question."]
#        },

#-----------------
# tag (nhãn lớp cho nội dung nhập của người dùng)
# patterns - mẫu câu đầu vào được training để phân lớp
# responses - các câu trả lời (bot) được mapping để hồi đáp những request trước đó.



import json
with open('data/intents.json') as json_data:
    intents = json.load(json_data)


# In[42]:


def ngrams(str, n):
    tokens = str.split(' ')
    arr = []
    for i in range(len(tokens)):
        new_str = ''
        if i == 0 and n>1:
            new_str = '_'
            for j in range(n):
                if j < n - 1:
                    if (i + j) <= len(tokens):
                        new_str += ' '+tokens[i+j]
                    else:
                        new_str += ' _'
        else:
            for j in range(n):
                if j < n:
                    if (i + j) < len(tokens):
                        if j == 0:
                            new_str += tokens[i+j]
                        else:
                            new_str += ' '+tokens[i+j]
                    else:
                        new_str += ' _'
        arr.append(new_str)
    return arr


# In[43]:


ngrams('a b c d e f g h', 4)


# In[3]:

# đánh lại nhãn các từ không có ý nghĩa
# ignore_words : danh sách các từ xuất hiện nhiều trong văn bản nhưng lại không có giá trị trong việc phân lớp

words = []
classes = []
documents = []
ignore_words = ['?', 'và', 'à', 'ừ', 'ạ', 'vì', 'từng', 'một_cách']

for intent in intents['intents']:
    for pattern in intent['patterns']:

        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)


# In[4]:


#Create training data
# chuyển dữ liệu Text sang dạng tensor number

training = []
output = []

output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])


# In[5]:


print(train_x[1])
print(train_y[1])


# In[6]:


tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('models/model.tflearn')


# In[8]:


import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "models/training_data", "wb" ) )

