⚠️ **Warning: Using this tool may result in your account being banned. Please consider carefully before using!** ⚠️


#### Support our community by clicking on the referral link below. Your contribution helps us continue improving and developing our bot. Thank you!
[Click here](https://t.me/tabizoobot/tabizoo?startapp=5833041671)

## Recommendation before use

# 🔥🔥 PYTHON version must be 3.10 🔥🔥


## Features  
|                      Feature                       | Supported |
|:--------------------------------------------------:|:---------:|
|                   Multithreading                   |     ✅     |
|              Proxy binding to session              |     ✅     |
| Auto-register your account with your referral link |     ✅     |
|             Auto claim, upgrade           |     ✅     |
|           Support for pyrogram .session            |     ✅     |


|        Settings         |                                 Description                                  |
|:-----------------------:|:----------------------------------------------------------------------------:|
|  **API_ID / API_HASH**  |   Platform data from which to run the Telegram session (default - android)   |
|       **AUTO UPGRADE**  |                             True/False                                       |
|       **USE_REF**       |         Register accounts with ur referral or not (default - False)          |
|       **REF_ID**        |   Your referral argument (comes after app/startapp? in your referral link)   |
| **USE_PROXY_FROM_FILE** | Whether to use a proxy from the `bot/config/proxies.txt` file (True / False) |

## Quick Start 📚

To fast install libraries and run bot - open run.bat on Windows or run.sh on Linux

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the API_ID and API_HASH provided after registering your application in the .env file.

## Installation
You can download the [**repository**](https://github.com/SkalaFrost/TabiZooBot.git) by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/SkalaFrost/TabiZooBot.git
cd TabiZooBot
```

Then you can do automatic installation by typing:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux manual installation
```shell
sudo sh install.sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/TabiZooBot >>> python3 main.py --action (1/2)
# Or
~/TabiZooBot >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```

You can also use arguments for quick start, for example:
```shell
~/TabiZooBot >>> python main.py --action (1/2)
# Or
~/TabiZooBot >>> python main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```




### Contacts

For support or questions, contact me on Telegram: 
[![Static Badge](https://img.shields.io/badge/telegram-bot_author-link?style=for-the-badge&logo=telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/airdropfactoryv)
