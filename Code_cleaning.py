
# coding: utf-8

# In[3]:

import nltk as nltk


# In[4]:

#Import stopwords and punctuation from NLTK
nltk.download("stopwords")
from string import punctuation
from nltk.corpus import stopwords


# In[5]:

#filtering out the stopwords and punctuations in the text called "raw"
#the new filtered text will be called "filtered_words"

filtered_for_punctuation = raw
for punc in punctuation:
    filtered_for_punctuation = filtered_for_punctuation.replace(punc, "")

tokens = nltk.wordpunct_tokenize(filtered_for_punctuation)

filtered_words = [word for word in tokens if word.lower() not in stopwords.words('english')]

