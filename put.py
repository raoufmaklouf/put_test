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
def cors_(url):
    
    headers={"Origin":"https://etdbeuajsyeu.com" ,'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1' }
    try:
        r=requests.get(url,headers=headers ,verify=False)
        origen=r.headers.get('Access-Control-Allow-Origin')
        credentials=r.headers.get('Access-Control-Allow-Credentials')
        if "https://etdbeuajsyeu.com" in str(origen) and 'true' in str(credentials):
            print('\033[91m Possibly CORS vulnerability\033[00m  '+url)
        else:
            pass
        r=requests.post(url, headers=headers ,verify=False)
        origen=r.headers.get('Access-Control-Allow-Origin')
        credentials=r.headers.get('Access-Control-Allow-Credentials')
        if "https://etdbeuajsyeu.com" in str(origen) and 'true' in str(credentials):
            print('\033[91m Possibly CORS vulnerability\033[00m  '+url)
        else:
            pass
    except:
        pass
def put(url):
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1'} 
    data="TFwKlsH7pVbfJ"
    filename='poc.html'
    url=url+'/'+filename
    print(url)
    try:
        r=requests.put(url, data, headers=headers, verify=False)
        scode=r.status_code
        print(scode)
        if "2" in str(scode):
            r=requests.get(url,headers=headers,verify=False)
            res=r.content
            if "TFwKlsH7pVbfJ" in str(res):
                print('\033[91m Possibly PUT methode Allow vulnerability\033[00m  '+url)
            else:
                pass
        else :
            pass
    except requests.exceptions.ConnectionError:
        pass
    
    

def main(word_queue):
    
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        attempt_list.append(attempt)

        for url in attempt_list:
           
           url=url.decode('utf-8')
           c_url1="http://"+url
           cors_(c_url1)
           c_url2="https://"+url
           cors_(c_url2)
           no_ssl_url='http://'+url
           put(no_ssl_url)
           ssl_url='https://'+url
           put(ssl_url)
           no_ssl_url2='http://'+url+':8080'
           put(no_ssl_url2)
           ssl_url2='https://'+url+':8443'
           put(ssl_url2)
        
        

    

word_queue = build_wordlist(raw_words)
for i in range(threads):
    t = threading.Thread(target=main,args=(word_queue,))
    t.start()







