#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep as snooze
from os import path, makedirs
from os.path import join
import pickle
import random
import string
import pathlib


#Declaring and assigning globals
global uname, pword, sex, bdaymonth, bdayday, bdayyear, amountOfTries, waitTime, successUrl, proxyURL, proxyEnabled, outputFolder;
uname="";pword="";sex="";bdaymonth="";successUrl="";proxyURL="";bdayday="";bdayyear="";amountOfTries=0;waitTime=0;outputFolder="";
proxyEnabled = False;

#Info
def setupUser(username, password=None, gender="Male", bdayMonth="Aug", bdayDay="07", bdayYear="2002"):
    global uname, pword, sex, bdaymonth, bdayday, bdayyear;
    uname = username
    if(password == None):
        pword = username[::-1]
    else:
        pword = password
    sex = gender #Female
    bdaymonth = bdayMonth
    bdayday = bdayDay
    bdayyear = bdayYear

def setupUserRandomized(password=None):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(12))
    setupUser(result_str, password)

def configIni(**kwargs):
    global amountOfTries, waitTime, successUrl, proxyURL, proxyEnabled, outputFolder;
    amountOfTries = 3  #5The amount of attempts to look for a successful account creation.
    waitTime = 10  #2The amount of time in seconds till it checks again for successful account creation.
    successUrl = "roblox.com/games"  #The url that is redirected to after a successful account creation. #https://www.roblox.com/games?SortFilter=default&TimeFilter=0
    proxyEnabled = False
    outputFolder = "accounts"

def createUser(proxy=False):
    global uname, pword, sex, bdaymonth, bdayday, bdayyear, amountOfTries, waitTime, successUrl, proxyURL, proxyEnabled;
    #executeableDriver = 'phantomjs.exe'
    chromeOptions = Options()
    #chromeOptions.add_argument("--headless")
    if(proxy):
        try:
            f = open("proxy.txt")
            f.close()
            f = open("proxy.txt", "r")
            Lines = f.read().splitlines()
            randomproxy = random.choice(Lines)
            print("Using proxy: " + randomproxy)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % randomproxy)
            browser = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install(), chrome_options=chrome_options)
        except FileNotFoundError:
            print("proxy.txt was not found. creating file...")
            f = open("proxy.txt", "x")
            f.close()
    else:
        print("proxy: False")
        browser = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install(), chrome_options=chromeOptions)
    #browser = webdriver.PhantomJS(executeableDriver)#,service_args=service_args
    browser.get("http://roblox.com")

    print("Name: {0}\nPassword :{1}\nGender: {2}\nMonth: {3}\nDay: {4}\nYear: {5}".format(uname,pword,sex,bdaymonth,bdayday,bdayyear),end="", flush=True)

    #Assigns different ids from the homepage variable names.
    usernameId = browser.find_element_by_id("signup-username")
    passwordId = browser.find_element_by_id("signup-password")
    gender = browser.find_element_by_id(sex+"Button")
    month = browser.find_element_by_id("MonthDropdown")
    day = browser.find_element_by_id("DayDropdown")
    year = browser.find_element_by_id("YearDropdown")

    #BDAY: Sets the birthdate.
    select = Select(month)
    select.select_by_value(bdaymonth)
    select = Select(day)
    select.select_by_value(bdayday)
    select = Select(year)
    select.select_by_value(bdayyear)

    #Uses the ids assigned before, clicks and types in boxes.
    usernameId.send_keys(uname);
    passwordId.send_keys(pword);
    gender.click()

    #Checks weather the registration was successful.
    CurrURL = browser.current_url
    print("\n" +CurrURL)
configIni()
#setupUserRandomized("testpasd")
#createUser(True)


'''
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
    '''
