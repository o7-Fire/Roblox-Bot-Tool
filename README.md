## Roblox-Bot-creator
Creates roblox accounts.

### How to Install
pip install RobloxAccountMaker

### Planning on being added
- --Proxy support-- done
- Check if username is taken
- Account Manager (other project)

### What does it do?
The program opens a script-controlled browser that navigates to the
roblox.com page, fills in every info, and lets you click the sign up
button and complete the captcha.

### How to use

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

```
## Proxy

```py
import RobloxAccountMaker

RobloxAccountMaker.setupUser("name123123", "password", "Male", "Jan", "04", "1990")
RobloxAccountMaker.createUser(True)
# True = enable proxy
# if not proxy.txt, then it will create one for you
```
![image](https://user-images.githubusercontent.com/46597698/110564811-6f6ecd80-8188-11eb-8660-124e3346dbc2.png)
![image](https://user-images.githubusercontent.com/46597698/110564867-831a3400-8188-11eb-8afa-f166ec408703.png)


Current use:

RobloxAccountMaker.setupUser(name, password, month, day, year)\
RobloxAccountMaker.setupUserRandomized(password)

What it looks like:

![image](https://user-images.githubusercontent.com/46597698/110479626-9396c400-8120-11eb-91bd-25c8cb04e0f7.png)
![image](https://user-images.githubusercontent.com/46597698/110479672-a01b1c80-8120-11eb-95cc-a5b65eb17192.png)

