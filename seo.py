#!/usr/bin/env python
# coding: utf-8

# In[28]:


from collections import Counter
from janome.tokenizer import Tokenizer
import pandas as pd
import numpy as np
import bs4
import re
import requests
import lxml.html as lx


word_list=[]
counts=pd.DataFrame()
t = Tokenizer()
dataset=[]

def get_word(query):
# query = 'テキスト'

    res = requests.get("URL"+ query)

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select('.st')
    p = re.compile(r"<[^>]*?>")
    full_text = p.sub("", str(elems))

    tokens = t.tokenize(full_text)


    for token in tokens:
        word = token.surface
        partOfSpeech = token.part_of_speech.split(',')[0]
        partOfSpeech2 = token.part_of_speech.split(',')[1]

        if partOfSpeech == "名詞":
            if (partOfSpeech2 != "非自立") and (partOfSpeech2 != "代名詞") and (partOfSpeech2 != "数"):
                word_list.append(word)
            
    word_list

    counter = Counter(word_list)
    return counter.most_common()

#     for count in counter.most_common():
#         counts=counts.append([list(count)],ignore_index=True)
#     dataset.append(counts)
# # print(dataset)

#     return dataset
    
    


# In[ ]:




