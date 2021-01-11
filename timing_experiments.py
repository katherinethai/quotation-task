import time
import spacy
from spacy.lang.en import English
from extraction import Extractor

frank_extract = Extractor(book_dir='frankenstein')

#start = time.time()
with open('frankenstein/frankenstein_docs/res000.txt','r') as f:
    text = f.read()

nlp = English()  # just the language with no model (idk this is spaCy stuff)
nlp.max_length = 3000000
sentencizer = nlp.create_pipe("sentencizer")
nlp.add_pipe(sentencizer)

doc = nlp(text)

with open('test.txt','w') as f:
    for sent in doc.sents:
        f.write(sent.text + '\n')
start = time.time()
with open('test.txt','r') as f:
    text = f.readlines()
end = time.time()

print(len(text))
time_elapsed = end-start
print('time elapsed:', time_elapsed)
