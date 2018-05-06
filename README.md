# Nexmo Telegram Bot

A simple Python app that integrates Nexmo API to Telegram Bot API. With this script you can send and receive messages from your Nexmo virtual number using a Telegram Bot.

A big thanks to [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot/), [nexmo-python](https://github.com/Nexmo/nexmo-python) and [flask](https://github.com/pallets/flask) for making such great open source tools.

**This is a fan-made Telegram Bot which is not supported by or associated with Nexmo.**

# How To Use

Open Python Console and run:
```python
pip install -r requirements.txt
```
Import the `app.py` to your project:
```python
from app import * 
```
Rename the file `config.ini.example` to `config.ini` and fill all the information.

```
[General]
host=YOUR_HOST
url_secret=YOUR_URL_SECRET
display_message=YOUR_DISPLAY_MESSAGE

[TelegramAPI]
chat_id=YOUR_CHAT_ID
api_token=YOUR_API_TOKEN

[NexmoAPI]
api_key=YOUR_API_KEY
api_secret=YOUR_API_SECRET
phone_number=YOUR_PHONE_NUMBER
```
# Settings
##### [General]
- **host**: Host where your webhook will be served.
- **url_secret**: Random string to secure your webhook endpoint.
- **display_message**: Message to be shown when acessing the endpoint via browser.

##### [TelegramAPI]
- **chat_id**: Your Telegram Chat ID. You can get it by deploying the application and sending the bot the command `/my_id`.
- **api_token**: Your Telegram Bot API Token.

##### [NexmoAPI]
- **api_key**: Your Nexmo API Key.
- **api_secret**: Your Nexmo API Secret.
- **phone_number**: Your Nexmo Virtual Phone Number.

Go to your Nexmo settings panel and [add your webhook URL in the settings](https://help.nexmo.com/hc/en-us/articles/206345667-How-do-I-add-a-webhook-URL-to-my-account-). Done.

# Bot usage

- **Send a new text message**: Use the command `/new` in this format `"/new phone_number text message here"`.
- **Reply to a text message**: Simply reply to the Telegram message.
- **Receive a text message**: Share your number with your friends and wait :D

# Release Notes
- **v0.0.2:**
    - Fix string parse
- **v0.0.1:**
    - First version

# FAQ
**Q: Where do I run this bot?**

A: I recommend using http://digitalocean.com/

**Q: Can you implement <???> function?**

A: I can try. Open a issue and I'll see what I can do.

**Q: Your bot is awesome. How can I help?**

A: Thank you! You can help by codding more features, creating pull requests, or donating using Bitcoin: **1BdL9w4SscX21b2qeiP1ApAFNAYhPj5GgG**

# License
----
MIT License

Copyright (c) 2018 blopa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

**Free Software, Hell Yeah!**