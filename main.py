import os
import string
import random
import uuid
import selenium
import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Email Gen
rand = uuid.uuid4()
link = 'fyii.de/trashmail/'
emil = '@fyii.de'
htmll= '.html'
str(rand)
str(link)
str(emil)
str(htmll)
emlink = str(link)+str(rand)+str(htmll)
print (emlink)
emaile =str(rand)+str(emil)
print (emaile)

#Name Gen (Adds a few seconds onto the time it takes to create an account but who fucking cares)
print ("Generating a name, should only take a sec!")
word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()

upper_words = [word for word in words if word[0].isupper()]
name_words  = [word for word in upper_words if not word.isupper()]
one_name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])


def rand_name():
   name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])
   return name


for n in range(1):
    name = rand_name()
    print(name)

#Launch Bot    
executable_path = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension('anticaptcha.crx')
#enable this if you wish
#chrome_options.add_extension('adblock.crx')
driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
driver.get("https://discordapp.com/register")


element = driver.find_element_by_name("email")
element.send_keys(emaile)

element = driver.find_element_by_name("username")
element.send_keys(name)

element = driver.find_element_by_name("password")
element.send_keys("deadasssecretpassword123")

element.send_keys(Keys.RETURN)

driver.get (str(link)+str(rand)+str(htmll))


