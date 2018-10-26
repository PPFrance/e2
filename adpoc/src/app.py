#-*- coding: utf-8 -*-
#
#
#
#
# Author: 

# Copyright (c) SomeCorp.

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


import sys
import requests
from logic import gen_relevant_data    
import re



REQUEST_TOKEN = 'GLOBAL!'
ACCESS_TOKEN = 'GLOBAL!'
#USER = 'GLOBAL!'
CONSUMER_KEY = '81245-4adff5d8772a6b2fe74ebd0f'
REDIRECT_URI = 'pockmarked81245:authorizationFinished'


@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')
    
@app.route('/authstart', methods=['GET'])
def obtain_request_token_then_redirect_user():
    """
    Steps 2 and 3 of https://getpocket.com/developer/docs/authentication
    
    2. Obtain a request token via call to pocket's API
    
    3. Redirect user to pocket to allow authorization/denial of this app. 
    
    Step 4 is the app redirecting back to this app's "authorized" route.
    We'll gloss over that, and invite the user simply to refresh to /authend
    
    """
    global REQUEST_TOKEN
    
    
    r = requests.post('https://getpocket.com/v3/oauth/request', 
                      {'consumer_key': CONSUMER_KEY, 'redirect_uri': REDIRECT_URI})
                      
    if not (r.status_code == 200 or len(r.split('=')) == 2):
        return f'Error, r.status_code: {r.status_code} and r.text: {r.text}', 201
        
    REQUEST_TOKEN = r.text.split('=')[1]
    print('request_token: {REQUEST_TOKEN}')
    #Or, e.g., marshmallow.
    
            
    pocket_auth_gui = f'https://getpocket.com/auth/authorize?request_token={REQUEST_TOKEN}&redirect_uri={REDIRECT_URI}'
        
    return redirect(pocket_auth_gui)
    
    
    
@app.route('/authend', methods=['GET'])
def get_access_token():
    """
    This does 5.
    """

    global ACCESS_TOKEN
    global USER
    
    r = requests.post('https://getpocket.com/v3/oauth/authorize', 
                      {'consumer_key': CONSUMER_KEY, 'code': REQUEST_TOKEN} )

    if not (r.status_code == 200):
        return f'Error, r.status_code: {r.status_code} and r.text: {r.text}', 201
       
       
    result = dict(map(tuple, [l.split('=') for l in r.text.split('&')]))
    
    ACCESS_TOKEN = result['access_token']
    #USER = result['user']
    
    return render_template('form.html')
        
    

@app.route('/decode', methods=['POST', 'GET'])
def pocketdecode():
    """
    This does the join between the list given from e.g., Remi's email and the content of the meta data from the API.
    """
    text = request.form['freeform_urls']
    pocket_ids_from_form = re.findall('https...app.getpocket.com.read.(\d+)', text, re.MULTILINE)
    
    
    r = requests.post('https://getpocket.com/v3/get', 
                      {'consumer_key': CONSUMER_KEY, 'access_token': ACCESS_TOKEN} )

    json_from_api = r.json()
    
    s = "<!doctype html><html lang=\"en\"><head></head><body>"
    s +="<table>"   
    for d in gen_relevant_data(pocket_ids_from_form, json_from_api):
        if 'not_found' in d:
            s += f"<tr><td colspan=3>Nothing was found in the user's account for article ID {d['not_found']}</td></tr>"
        else:
            url = '"' + d['resolved_url'] + '"'
            
            #print (f"<tr><td>{d['resolved_title']}</td><td></td><td>{d['time_to_read']} mins</td><td>{d['word_count']} words</td></tr>")
            #print (f"<tr><td colspan=3><strong>{d['excerpt']}</strong></td></tr>")
            s += f"<tr><td colspan=3><a href={url}>{d['resolved_url']}</a></td></tr>"
    s += "</table>"
    s += "</body></html>"    
        
        
    return s


@app.route('/putinpocket', methods=['GET'])
def pocketencode():
    """
    
    """
    
    import bs4
    bs = bs4.BeautifulSoup(open('/Users/PeterParkinson/Downloads/ril_export.html'))
    
    class Link:
        def __init__(self, url, tags = ''):
            self.url = url
            self.tags = 'remi,' + tags
            
        def __str__(self):
            return f'link: {self.url}, tags: {self.tags}'
    
    def linkGen(bs):
        for l in bs.findAll('a', attrs={'href': re.compile("//")}):
            link = Link(l.attrs['href'], l.attrs['tags'])
            
            print (f'about to yield: {link}', file=sys.stderr)
            
            yield link
            
    
    from pocket import Pocket
    pock = Pocket(access_token=ACCESS_TOKEN, consumer_key=CONSUMER_KEY)
    
    for link in linkGen(bs):
        pock.bulk_add(url=link.url, tags=link.tags)
        
    pock.commit() 
        
        
    return ''



if __name__ == '__main__':
    
    app.run(host='127.0.0.1', debug=True)
    