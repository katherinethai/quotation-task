import os

def generate_script(book_dir, doc_filename, save_to_folder = 'windows'):
    doc_path = os.path.join(book_dir, book_dir + '_docs','sents',doc_filename)
    with open('grep_files.sh','w') as f:
        f.write('#!/bin/bash \n\n\n')
        with open('frankenstein_sentences.txt','r') as sents_file:
            sents = sents_file.readlines()
            for i,sent in enumerate(sents):
                sent = sent.replace("!","\!")
                sent = sent.replace("(","\(")
                sent = sent.replace(")","\)")
                sent = sent.replace("[","\[")
                sent = sent.replace("]","\]")
                sent = sent.replace(";","\;")
                sent = sent.replace("\"",'\\"')
                sent = sent.replace("'","\\'")
                sent = "\"" + sent + "\""
                # if '\"' in sent:
                #     sent = sent.replace("'","\\'")
                #     sent = '\'' + sent + '\''
                # else:
                #     #sent = sent.replace("'","\\'")
                #     sent = '\"' + sent + '\"'
                window_filename = book_dir + '-' + str(i) + '.txt'
                f.write('grep -C 5 ' + sent.replace('\n','') + ' ' + doc_path + ' > ' + window_filename)
                f.write('\n')

generate_script('frankenstein','res000-sents.txt')
