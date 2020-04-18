import requests
import threading
import queue
import sys
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


f=sys.argv[1]
threads =100
fd = open(f,"rb")
raw_words = fd.readlines()
fd.close() 
def build_wordlist(raw_words):
    
    words= queue.Queue()
    for word in raw_words:
        word = word.rstrip()
        words.put(word)
        
    return words

def request_(url):
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1'} 
    data="TFwKlsH7pVbfJ"
    filename='poc.html'
    url=url+'/'+filename
    try:
        r=requests.put(url, data, headers=headers, verify=False)
        scode=r.status_code
        if "2" in str(scode):
            r=requests.get(url,headers=headers,verify=False)
            res=r.content
            if "TFwKlsH7pVbfJ" in str(res):
                print('\033[91m Possibly PUT methode Allow vulnerability\033[00m  '+url)
            else:
                print('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
        else :
            pass
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    

def main(word_queue):
    
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        attempt_list.append(attempt)

        for url in attempt_list:
           
           url=url.decode('utf-8')
           print(url)
           no_ssl_url='http://'+url
           request_(no_ssl_url)
           ssl_url='https://'+url
           request_(ssl_url)
           no_ssl_url2='http://'+url+':8080'
           request_(no_ssl_url2)
           ssl_url2='https://'+url+':8443'
           request_(ssl_url2)
        
        

    

word_queue = build_wordlist(raw_words)
for i in range(threads):
    t = threading.Thread(target=main,args=(word_queue,))
    t.start()



