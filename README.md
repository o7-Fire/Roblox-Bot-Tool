## Roblox-Bot-creator
Creates roblox accounts.

### Note from the author
- The project has been cancelled long ago.
- If you want to make use of it try learning some python, it really isn't that difficult :), some resources:

https://www.python.org/about/gettingstarted/

https://www.learnpython.org/

Knock yourself out! Good luck

### Planning on being added
- Proxy support
- Check if username is taken
- Star, Follow, Like (Generally control bots)
- Account Manager (other project)

### What does it do?
The program opens a script-controlled browser that navigates to the roblox.com page, then it signs up.

### Error sources and bugs
- Captcha Confirmation (Begins popping up after you've tried a couple times with same IP/proxy)
- Username Taken (Not handled currently)

### How to use
Open python interpretter in main directory
```
>>> import RobloxAccountMaker as rm
>>> rm.setupUser("kresten123", "password", "Male", "Aug", "7", "2002")
>>> rm.createUser()
or
>>> import RobloxAccountMaker as rm
>>> rm.setupUserRandomized("password")
```
