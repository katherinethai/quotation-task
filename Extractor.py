import spacy
import os
from spacy.lang.en import English
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import multiprocessing as mp

class Extractor():
    def __init__(self, book_dir, save_to_folder = 'windows'):
        self.book_dir = book_dir
        self.book_filename = book_dir + '_sentences.txt'
        self.book_sentences = self.get_book_sentences()
        self.results_dir = self.book_dir + '_docs'
        self.results_filenames = os.listdir(os.path.join(self.book_dir,self.results_dir))
        self.nlp = self.get_nlp()
        self.save_to_folder = save_to_folder
        self.window_count = 0

    def txt_file_to_doc(self, filename):
        with open(filename,'r') as f:
            text = f.read()
        return self.nlp(text)

    def get_book_sentences(self):
        with open(os.path.join(self.book_dir, self.book_filename),'r') as f:
            text = f.readlines()
        return text

    def get_nlp(self):
        nlp = English()  # just the language with no model (idk this is spaCy stuff)
        nlp.max_length = 5000000
        sentencizer = nlp.create_pipe("sentencizer")
        nlp.add_pipe(sentencizer)
        return nlp

    def find_fuzzy_match(self, book_sent, secondary_source):
        choices = [sent for sent in doc.sents]
        match = process.extractOne(book_sent, choices, scorer=fuzzwuzz.base_ratio, score_cutoff=90)
        span = match[0]


    def extract_fuzzy_window_parallel(self):
        pool = mp.Pool(mp.cpu_count()/2)
        results = [pool.apply_asynch(self.extract_windows, args=())]

        def cube(x):
    return x**3
pool = mp.Pool(processes=4)
results = [pool.apply(cube, args=(x,)) for x in range(1,7)]

frank_extract = Extractor(book_dir='frankenstein')
secondary_source = frank_extract.txt_file_to_doc('frankenstein/frankenstein_docs/res0.txt')
