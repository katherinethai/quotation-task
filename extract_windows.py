import spacy
import os
from spacy.lang.en import English
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

nlp = English()  # just the language with no model
nlp.max_length = 1500000
sentencizer = nlp.create_pipe("sentencizer")
nlp.add_pipe(sentencizer)
with open('res1.txt','r') as f:
     text = f.read()
# with open('res2.txt','r') as f:
#      text += ' ' + f.read()
# with open('res3.txt','r') as f:
#      text += ' ' + f.read()
# print(text)
doc = nlp(text)


# query = 'Remember, I am not recording the vision of a madman.'
# choices = [sent for sent in doc.sents]
#
# matches = process.extract(query, choices, limit=1)
# print(len(matches))
# print(matches[0][0].start,matches[0][0].end)
# for match in matches:
#     # print(doc[match[0].start-10:match[0].end+10])
#     print(match)
