#! /usr/bin/python3
import re, os, codecs
from os.path import isfile, join
from bs4 import BeautifulSoup

def html_parser2(src_dir):
    threads = 0
    messages = 0
    text_name = src_dir + '_text'
    output_file = codecs.open('raw_texts/'+text_name, mode='w+', encoding='cp1251')
    for file in os.listdir(src_dir):
        if isfile(join(src_dir, file)):
            f=open(os.path.join(src_dir, file), 'r')
            soup = BeautifulSoup(f)
            bq = soup.find_all('blockquote')
            if len(bq) == 0:
                continue
            for el in bq:
                x = ''
                x = join(x,el.get_text())
                x = re.sub('>>\d+', '', x)
                x = re.sub('\n', '',x)
                output = x +' .'
                output_file.write(output)   
                messages += 1
            threads +=1
    output_file.close()
    print (str(threads)+ ' threads, '+str(messages) +' messages.')
    return threads, messages

html_parser2("4chan")
html_parser2("2ch")
html_parser2("iichan")
html_parser2("krautchan")
