import nltk

import pickle


#for creating the spam_corpus and ham_corpus below,
#i couldn't find a way to set/change the working directory...
#so i just specified the full path location where my files are.

spam_corpus = nltk.corpus.PlaintextCorpusReader('C:/Users/User/Box Sync/2017 - Winter/LIN127 Corpus & Text Analysis/Homework/HW 2/SPAM_training','SPAM.*.txt')

ham_corpus = nltk.corpus.PlaintextCorpusReader('C:/Users/User/Box Sync/2017 - Winter/LIN127 Corpus & Text Analysis/Homework/HW 2/SPAM_training','HAM.*.txt')

ham_count = len(ham_corpus.fileids())

spam_count = len(spam_corpus.fileids())


spam_fd = nltk.FreqDist(spam_corpus.words())

ham_fd = nltk.FreqDist(ham_corpus.words())


model = {
 'ham_count': ham_count,
 'spam_count': spam_count,
 'ham_fd': ham_fd,
 'spam_fd': spam_fd
}


pickle.dump(model, open('spam.nb', 'wb'))
