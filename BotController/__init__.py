#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import sleep as snooze
from Debug import Log as log

global uname, pword, sex, bdaymonth, bdayday, bdayyear, amountOfTries, waitTime, successUrl, proxyURL, proxyEnabled;
uname="";pword="";sex="";bdaymonth="";successUrl="";proxyURL="";bdayday="";bdayyear="";amountOfTries=0;waitTime=0;
proxyEnabled = False;

#Info
def setupUser(username, password=None, gender="Male", bdayMonth="Aug", bdayDay="7", bdayYear="2002"):
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

def configIni(**kwargs):
    global amountOfTries, waitTime, successUrl, proxyURL, proxyEnabled;
    amountOfTries = 5  #The amount of attempts to look for a successful account creation.
    waitTime = 2  #The amount of time in seconds till it checks again for successful account creation.
    successUrl = "roblox.com/games"  #The url that is redirected to after a successful account creation.
    proxyURL = "140.227.81.53:3128"
    proxyEnabled = False

def createUser():
    global uname, pword, sex, bdaymonth, bdayday, bdayyear, amountOfTries, waitTime, successUrl, proxyURL, proxyEnabled;
    executeableDriver = 'chromedriver.exe'
    #executeableDriver = 'phantomjs.exe'

    #chromeOptions = Options()
    #chromeOptions.add_argument("--headless")

    if(proxyEnabled):
        service_args = [
        '--proxy={}'.format(proxyURL),
        '--proxy-type=socks5',
        ]
    else:
        service_args = []

    browser = webdriver.Chrome(executeableDriver)
    #browser = webdriver.PhantomJS(executeableDriver)#,service_args=service_args
    browser.get('https://www.roblox.com')

    print("{0}:{1}:{2}:{3}/{4}-{5}".format(uname,pword,sex,bdaymonth,bdayday,bdayyear),end="", flush=True)

    #Ids and classes
    usernameId = browser.find_element_by_id("signup-username")
    passwordId = browser.find_element_by_id("signup-password")
    password2Id = browser.find_element_by_id("signup-password-confirm")
    #termsofService = browser.find_element_by_xpath("//*[@id="agreeTermsPrivacyLabel"]").click() #//*[@id="agreeTermsPrivacyLabel"]
    gender = browser.find_element_by_id(sex+"Button")
    month = browser.find_element_by_id("MonthDropdown")
    day = browser.find_element_by_id("DayDropdown")
    year = browser.find_element_by_id("YearDropdown")

    #BDAY:
    select = Select(month)
    select.select_by_value(bdaymonth)
    select = Select(day)
    select.select_by_value(bdayday)
    select = Select(year)
    select.select_by_value(bdayyear)

    usernameId.send_keys(uname);
    passwordId.send_keys(pword);
    password2Id.send_keys(pword);
    gender.click()
    browser.find_element_by_xpath('//*[@id="agreeTermsPrivacyLabel"]').click() #//*[@id="agreeTermsPrivacyLabel"]

    browser.find_element_by_xpath('//*[@id="signup-button"]').click()

    CurrURL = browser.current_url
    log(CurrURL)
    tries = 0
    while not successUrl in CurrURL:
        if(tries < amountOfTries):
            CurrURL = browser.current_url
            log("Trying again, Tries: {0}/{1}; URL: {2}".format(tries, amountOfTries, CurrURL))
            snooze(waitTime)
            tries += 1
        else: break;
    #browser.save_screenshot('screen.png')
    if(successUrl in CurrURL):
        #Created account successfully.
        print("...Account was created.")
    else:
        #Failed in creating account.
        print("...Account could not be created. Landing page: {}".format(CurrURL))
    browser.save_screenshot('screenEnd.png')
    #browser.quit()

#setupUser("JorgeCrawford39")
#configIni()
#createUser()