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
```
>>> import RobloxAccountMaker as rm
>>> rm.setupUser("kresten123", "password", "Male", "Aug", "7", "2002")
>>> rm.createUser()
or
>>> import RobloxAccountMaker as rm
>>> rm.setupUserRandomized("password")
>>> rm.createUser()
```

Current use:

RobloxAccountMaker.setupUser(name, password, month, day, year)
RobloxAccountMaker.setupUser(name)
RobloxAccountMaker.setupUserRandomized(password)
RobloxAccountMaker.setupUserRandomized()

What it looks like:

![image](https://user-images.githubusercontent.com/46597698/110476930-87f5ce00-811d-11eb-8cf2-8e230ad5c11d.png)
