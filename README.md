## Roblox-Bot-creator
Creates roblox accounts.

### How to Install

pip install RobloxAccountMaker

### Note from the author
- The project has been cancelled long ago.
- If you want to make use of it try learning some python, it really isn't that difficult :), some resources:

https://www.python.org/about/gettingstarted/

https://www.learnpython.org/

Knock yourself out! Good luck

### Planning on being added
- Proxy support
- Check if username is taken
- Account Manager (other project)

### What does it do?
The program opens a script-controlled browser that navigates to the
roblox.com page, fills in every info, and lets you click the sign up
button and complete the captcha.

### How to use
Open python interpretter in main directory

```py
import RobloxAccountMaker

RobloxAccountMaker.setupUser("name123123", "password", "Male", "Jan", "04", "1990")
RobloxAccountMaker.createUser()

#creates account with randomized name 
RobloxAccountMaker.setupUserRandomized("password")
RobloxAccountMaker.createUser()

#creates account with randomized name and password is name
RobloxAccountMaker.setupUserRandomized()
RobloxAccountMaker.createUser()

``

Current use:

RobloxAccountMaker.setupUser(name, password, month, day, year)
RobloxAccountMaker.setupUser(name)
RobloxAccountMaker.setupUserRandomized(password)
RobloxAccountMaker.setupUserRandomized()

What it looks like:

![image](https://user-images.githubusercontent.com/46597698/110476930-87f5ce00-811d-11eb-8cf2-8e230ad5c11d.png)
