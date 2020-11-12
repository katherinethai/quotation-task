import spacy
from spacy.lang.en import English
import math
import numpy as np

nlp = English()
tokenizer = nlp.Defaults.create_tokenizer(nlp)

def split_txt(res):
    with open('../yapeichang/frankenstein/frankenstein_docs/' + res) as f:
        text = f.read()
    tokens = tokenizer(text)

    nearest_10 = int(math.ceil(len(tokens) / 10.0) * 10)
    intervals = np.linspace(0, nearest_10, int(nearest_10/10), endpoint=False)
    intervals = [int(x) for x in intervals]

    output = open('frankenstein/frankenstein_docs/' + res, "w")

    for i in intervals:
        if i != intervals[-1]:
            output.write(tokens[i:i+10].as_doc().text)
            output.write("\n")
        else:
            output.write(tokens[i:len(tokens)].as_doc().text)
    output.close()


for i in range(211):
    filename = 'res' + str(i+2) + '.txt'
    print(filename)
    split_txt(filename)
