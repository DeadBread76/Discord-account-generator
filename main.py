import os
import string
import random
import uuid
import selenium
import requests
import urllib.request
import time
from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask


#Anti Captcha info
api_key = 'key_here'
site_key = 'nubQ83kz2YYRrleJaYf_CYbvDZ6lXVl-NL_MWX1Uj9Y'

#Email Gen
rand = str(uuid.uuid4())
link = 'fyii.de/trashmail/' # when using quotes it will be a string see function above if you want your variables to be integers or strings.
email_address = '@fyii.de'
email_link = link+rand+'.html'
email = rand+email_address
print(email+'\n'+email_link) # just make things neater :D

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
element.send_keys(email)

element = driver.find_element_by_name("username")
element.send_keys(name)

element = driver.find_element_by_name("password")
element.send_keys(rand)

element.send_keys(Keys.RETURN)

url = 'https://discordapp.com/register'
client = AnticaptchaClient(api_key)
task = NoCaptchaTaskProxylessTask(url, site_key)
job = client.createTask(task)
print("Waiting for solution from AntiCaptcha")
job.join()
response = job.get_solution_response()
print("Received solution", response)
driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"' % response)

driver.find_element_by_xpath('//button[@type="submit" and @class="btn-std"]').click()
