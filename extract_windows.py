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


query1 = 'I had desired it with an ardour that far exceeded moderation; but now that I had finished, the beauty of the dream vanished, and breathless horror and disgust filled my heart.'
query2 = 'Unable to endure the aspect of the being I had created, I rushed out of the room, and continued Vol. I.-29 e442 MISCELLANIES BY SIR WALTER SCOTT. a long time traversing my bed-chamber, unable to compose my mind to sleep.'
choices = [sent for sent in doc.sents]

matches = process.extract(query1, choices, limit=1)
print(matches[0][0].start,matches[0][0].end)
for match in matches:
    print(doc[match[0].start:match[0].end])
matches = process.extract(query2, choices, limit=1)
print(matches[0][0].start,matches[0][0].end)
for match in matches:
    print(doc[match[0].start:match[0].end])
