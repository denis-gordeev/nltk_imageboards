#!/usr/bin/python3.2
#save fourchan pages
from urllib.request import urlopen
from re import findall, sub
import http.client
from urllib.parse import urlparse
import time
def save_site():
    
    def checkUrl(url):
        print(url)
        p = urlparse(url)
        conn = http.client.HTTPConnection(p.netloc)
        conn.request('HEAD', p.path)
        resp = conn.getresponse()
        return resp.status < 404
    def write_html(url, site_folder, string_index=0):
        site_page = urlopen(url)
        str_site = ''
        if string_index == 0:
            str_site = str(site_page.read())
        else:
            str_site = str(site_page.readlines()[string_index])
        threads = []
        if site_folder == "krautchan/":
            threads = findall('thread-\d+',str_site)
        else:
            threads = findall('res/\d+', str_site)
        threads = set(threads)
        print(threads)
        for thread in threads:
            if checkUrl(url+thread+'.html'):
                print('saved')
                thread_page = urlopen(url+thread+'.html')
                thread_name = sub('res/', '',thread)
                thread_text = thread_page.read()
                thread_file = open(site_folder+thread_name+'.html', 'w+')
                thread_file.write(thread_text.decode('utf-8'))
            else:
                continue
    write_html("http://boards.4chan.org/b/", '4chan/')

    write_html("http://iichan.hk/b/", "iichan/")

    write_html("http://2ch.hk/b/",'2ch/')

    write_html("http://krautchan.net/b/", "krautchan/")
    time.sleep(180)

while True:
    save_site()
