from flask import Flask, request, jsonify
import telegram
import nexmo
import json
import configparser

# Config parsers
Config = configparser.ConfigParser()
Config.read("config.ini")

# CONFIG
DISPLAY_MESSAGE = Config.get('General', 'display_message')
HOST = Config.get('General', 'host')
URL_SECRET = Config.get('General', 'url_secret')
TELEGRAM_CHAT_ID = Config.get('TelegramAPI', 'chat_id')
TELEGRAM_TOKEN = Config.get('TelegramAPI', 'api_token')
NEXMO_API_KEY = Config.get('NexmoAPI', 'api_key')
NEXMO_API_SECRET = Config.get('NexmoAPI', 'api_secret')
NEXMO_MY_NUMBER = Config.get('NexmoAPI', 'phone_number')

application = Flask(__name__)
bot = telegram.Bot(TELEGRAM_TOKEN)
bot.setWebhook(webhook_url='https://%s/nexmo/telegram%s' % (HOST, URL_SECRET))
nexmo_client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

@application.route('/nexmo')
def index():
	return DISPLAY_MESSAGE

@application.route('/nexmo/telegram' + URL_SECRET, methods=['POST'])
def telegram_webhook():
	update = telegram.update.Update.de_json(request.get_json(force=True), bot)
	if update.message.text == '/my_id':
		bot.sendMessage(chat_id=update.message.chat_id, text='Your Telegram ID is ' + str(update.message.chat_id))
	elif update.message.chat_id == int(TELEGRAM_CHAT_ID):
		if update.message.reply_to_message is not None:
			data = update.message.reply_to_message.text.splitlines()
			to = data[0].replace('From: ', '')
			sender = data[1].replace('To: ', '')
			if to and sender:
				bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text='Trying to send your message...')
				# Sending message
				response = nexmo_client.send_message({'from': sender, 'to': to, 'text': update.message.text})
				response = response['messages'][0]
				if response['status'] == '0':
					message = 'YAY! Message sent!\nID: %s\nRemaining balance: %s' % (response['message-id'], response['remaining-balance'])
					bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=message)
				else:
					bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text='Error: ' + response['error-text'])
			else:
				bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text='This is not a valid reply.')
		elif update.message.text.startswith('/new'):
			params = update.message.text.split()
			if len(params) >= 3 and params[0] == '/new':
				to = params[1]
				sender = NEXMO_MY_NUMBER
				message = update.message.text.replace(params[0] + ' ' + params[1], '')
				if to and sender and message:
					bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text='Trying to send your message...')
					# Sending message
					response = nexmo_client.send_message({'from': sender, 'to': to, 'text': message})
					response = response['messages'][0]
					if response['status'] == '0':
						message = 'YAY! Message sent!\nID: %s\nRemaining balance: %s' % (response['message-id'], response['remaining-balance'])
						bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=message)
					else:
						bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text='Error: ' + response['error-text'])
				else:
					bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text='This is not a valid command.')
			else:
				bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text='Incorrect data.')
		else:
			bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=update.message.text + ' :D')

	return ('', 204)

@application.route('/nexmo/sms' + URL_SECRET, methods=['GET', 'POST'])
def nexmo_webhook():
	if request.is_json:
		text_message = format_message(request.get_json())
		bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=text_message, parse_mode='HTML')
		# pprint(request.get_json())
	else:
		data = dict(request.form) or dict(request.args)
		text_message = format_message(data)
		bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=text_message, parse_mode='HTML')
		# pprint(data)

	return ('', 204)

def format_message(json):
	reply = '' # '(reply this message to reply)'
	sender = json['msisdn'][0]
	receiver = json['to'][0]
	date = json['message-timestamp'][0]
	content = json['text'][0]
	return '<b>%s</b>\n<b>From: %s</b>\n<b>To: %s</b>\n<b>On: %s</b>\n\n%s' % (reply, sender, receiver, date, content)
