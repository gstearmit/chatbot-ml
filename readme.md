### Chatbot with Machine Learning

#### Training Model
```
python3 training.py
```
#### Predict
```
from predict import response, classify

>>> response('is your shop open today?')
We're open every day from 9am-9pm

>>> classify('is your shop open today?')
[('opentoday', 0.93861651)]
```


-------MacOS Install pip3 ----------------

   $ curl -O https://bootstrap.pypa.io/get-pip.py

   $ sudo python3 get-pip.py

Cai Cac Thu Vien chay cho python3

    $ sudo pip3 install -U nltk
    $ sudo pip3 install -U numpy
    $ sudo pip3 install -U tflearn



TensorBroad :

      $ tensorboard --logdir="./tflearn_logs" --port 6006

Fixed Error : "Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA"

     import os
     os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


Step 7: Install Tensorflow and other dependencies

$ pip3 install -r requirements.txt