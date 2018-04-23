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