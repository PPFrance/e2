# coding: utf-8
from selenium import webdriver 

import os
import time
import re
import sys

import bs4


def remi_export_link_gen(filename = '/Users/PeterParkinson/Downloads/ril_export-3.html'):
    bs = bs4.BeautifulSoup(open(filename))
    
    for l in bs.findAll('a', attrs={'href': re.compile("//")}):
        link = l.attrs['href']
   
        print (f'about to yield: {link}', file=sys.stderr)
        
        yield link
        



class PocketAutomator:
    def __init__(self, username=os.environ['POCKET_USERNAME'], password=os.environ['POCKET_PASSWORD']):
        self.driver = webdriver.Safari()  
        self.username = username
        self.password = password
        self.driver.get('https://getpocket.com/a/queue/')
        
    def login(self): 
        un = self.driver.find_element_by_name('username')
        un.click()
        un.send_keys(self.username)
        pw = self.driver.find_element_by_name('password')
        pw.click()
        pw.send_keys(self.password)
        sm = self.driver.find_element_by_class_name('login-btn-email')
        sm.click()


    def save_url(self, url):
        
        time.sleep(5)
        a = self.driver.find_element_by_css_selector('#pagenav_addarticle').find_element_by_css_selector('a')
        a.click()
        
        
        time.sleep(1)
        url_input = self.driver.find_element_by_css_selector('#addMenu').find_element_by_css_selector('input')
        url_input.send_keys(url)
        
        add_btn = self.driver.find_element_by_css_selector('#addMenu').find_element_by_css_selector('.button')
        time.sleep(1)
        add_btn.click()
        
        

   
        
if __name__=='__main__':
    
    pa = PocketAutomator()
    
    pa.login()
    
    for url in remi_export_link_gen():
        pa.save_url(url)
        print (f'Saved "{url}" to pocket', file=sys.stderr)
 
 
    print (f'Done, exiting.')
   

"""   
a = driver.find_element_by_css_selector('#pagenav_addarticle').find_element_by_css_selector('a')
a.click()


url_input = driver.find_element_by_css_selector('#addMenu').find_element_by_css_selector('input')
url_input.send_keys(url)

add_btn = driver.find_element_by_css_selector('#addMenu').find_element_by_css_selector('.button')
add_btn.click()
"""
