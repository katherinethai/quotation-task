import spacy
import os
from spacy.lang.en import English
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

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

    def get_book_sentences(self):
        with open(os.path.join(self.book_dir, self.book_filename),'r') as f:
            text = f.readlines()
        return text

    def get_nlp(self):
        nlp = English()  # just the language with no model (idk this is spaCy stuff)
        nlp.max_length = 3000000
        sentencizer = nlp.create_pipe("sentencizer")
        nlp.add_pipe(sentencizer)
        return nlp

    def extract_windows(self):
        if not os.path.exists(os.path.join(self.book_dir, self.save_to_folder)):
            os.makedirs(os.path.join(self.book_dir, self.save_to_folder))
        for result in self.results_filenames:
            res_filename = os.path.join(self.book_dir, self.results_dir, result)
            with open(res_filename,'r') as f:
                text = f.read()
            doc = self.nlp(text)
            choices = [sent for sent in doc.sents]
            for book_sent in self.book_sentences:
                print(book_sent)
                query = book_sent
                matches = process.extract(query, choices, limit=1)
                for match in matches:
                    filename = self.book_dir + '-' + str(self.window_count) + '.txt'
                    path = os.path.join(self.book_dir, self.save_to_folder, filename)
                    span = match[0]
                    score = match[1]
                    if score > 90:
                        self.window_count += 1
                        with open(path,'w') as writer:
                            window = doc[span.start-100:span.end+100].as_doc().text
                            writer.write(window)

frank_extract = Extractor(book_dir='frankenstein')
frank_extract.extract_windows()
