#!/usr/bin/env python
# coding: utf-8

# # Naive Bayes classifier

# In[1]:


reviews=[['he likes the restaurant'],['he dislikes the restaurant'],['wonderful restaurant'],
         ['great service and fantastic food']]
labels=['positive','negitive','positive','positive' ]


#   ### function to return the number of all unique words in the training set

# In[2]:


def get_length_of_unique_words(corpus):
   
    s=set()
    str_ = ''
    for i in corpus:
    
        for word in i: 
             str_ += word 
    a=str_.split()
    for i in a:
        s.add(i)
    return len(s)          


# In[3]:


V=get_length_of_unique_words(reviews)
print(V)


#  #### function to return the number of all words in given class

# In[4]:


def get_length_of_all_words_for_given_class(corpus,All_labels, given_class):
    
    global a
    s=0
 
    for i,j in zip(corpus,All_labels):
        if j==given_class:
            a=get_length_of_unique_words(i)
            s+=a
        
    return (s)


# In[5]:


## Test your code to validate the results
all_words_len_for_negitive_class=get_length_of_all_words_for_given_class(reviews,labels, given_class='negitive')
print(all_words_len_for_negitive_class)


all_words_len_for_positive_class=get_length_of_all_words_for_given_class(reviews,labels, given_class='positive')
print(all_words_len_for_positive_class)


# #### function to return the occurance of given word in spcific class

# In[6]:


def get_of_occurance_of_word_in_given_class(word,corpus,labels, given_class):
    
    s=''
    l=0
    tot=0
    for i,j in zip(corpus,labels):
        if j==given_class:
    
            for w in i:
                s+= w
            a=list(s.split())
            if word in a:
                l+=1
    tot+=l        
    return tot


# In[7]:


occurance=get_of_occurance_of_word_in_given_class( 'restaurant',reviews, labels,given_class='negitive')
occurance


# #### function to calculate the prior probablity for given class

# In[8]:


def get_prior_prob(c):
    
    s= len([w for w in labels if w == c ])/len(labels)

    
    return s


# In[9]:


print(get_prior_prob('negitive'))


# #### function to caclulate the likelihood for a word given a class p(word|class)

# In[10]:


## p(word|class)

def get_likelihood_for_given_word(corpus, all_labels, word, given_class):
    V=get_length_of_unique_words(corpus)
    Len_of_all_words_for_given_class=get_length_of_all_words_for_given_class(corpus,all_labels, given_class)
    occurance_ =get_of_occurance_of_word_in_given_class(word, corpus, all_labels, given_class)
    
    ## apply the formula
    likeihood=(occurance_+1)/(Len_of_all_words_for_given_class+V)
    return likeihood
  


# In[11]:


likeihood=get_likelihood_for_given_word(reviews, labels, 'restaurant', 'negitive')
print(likeihood)


# In[ ]:




