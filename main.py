import telebot
from telebot import types
from database import Database

bot = telebot.TeleBot('5415524055:AAGHGAKYir7R-O1His9uLyTDksB_OXQ917k')
db = Database('mero2', 'postgres', '240816', 'localhost')
db.clear_table('users')
STAGES = 10

@bot.message_handler(commands=['start'])
def start(message):
	if not db.user_exist(message.chat.id):
		db.add_user(message.chat.id)
		markupInline = types.InlineKeyboardMarkup()
		hello = types.InlineKeyboardButton(text='Будем знакомы', callback_data='hello')
		markupInline.add(hello)
		mes_text = load_text('start')
		bot.send_photo(message.chat.id, photo=open('img/1.png',  'rb'), caption=mes_text, reply_markup=markupInline)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
	if call.data == 'team1':
		send_first_road_message(call.message.chat.id, call.message.message_id, 1)
	elif call.data == 'team2':
		send_first_road_message(call.message.chat.id, call.message.message_id, 2)
	elif call.data == 'team3':
		send_first_road_message(call.message.chat.id, call.message.message_id, 3)
	elif call.data == 'team4':
		send_first_road_message(call.message.chat.id, call.message.message_id, 4)
	elif call.data == 'team5':
		send_first_road_message(call.message.chat.id, call.message.message_id, 5)
	elif call.data == 'team6':
		send_first_road_message(call.message.chat.id, call.message.message_id, 6)
	elif call.data == 'team7':
		send_first_road_message(call.message.chat.id, call.message.message_id, 7)
	elif call.data == 'team8':
		send_first_road_message(call.message.chat.id, call.message.message_id, 8)
	elif call.data == 'team9':
		send_first_road_message(call.message.chat.id, call.message.message_id, 9)
	elif call.data == 'team10':
		send_first_road_message(call.message.chat.id, call.message.message_id, 10)

	elif call.data == 'hello':
		mes_text = load_text('hello')
		img  = open('img/2.jpg', 'rb')
		send_question_message(call.message.chat.id, call.message.message_id, mes_text, img)
	elif call.data == 'what_is_key':
		mes_text = load_text('what_is_key')
		img = open('img/2.jpg', 'rb')
		send_question_message(call.message.chat.id, call.message.message_id, mes_text, img)
	elif call.data == 'how_do_tasks':
		mes_text = load_text('how_do_tasks')
		img = open('img/1.png', 'rb')
		send_question_message(call.message.chat.id, call.message.message_id, mes_text, img)
	elif call.data == 'how_get_keys':
		mes_text = load_text('how_get_keys')
		img = open('img/1.png', 'rb')
		send_question_message(call.message.chat.id, call.message.message_id, mes_text, img)
	elif call.data == 'any_questions':
		mes_text = load_text('any_questions')
		img = open('img/1.png', 'rb')
		send_question_message(call.message.chat.id, call.message.message_id, mes_text, img)

	elif call.data == 'start_game':
		markupInline = types.InlineKeyboardMarkup()
		team1 = types.InlineKeyboardButton(text='Команда 1', callback_data='team1')
		team2 = types.InlineKeyboardButton(text='Команда 2', callback_data='team2')
		team3 = types.InlineKeyboardButton(text='Команда 3', callback_data='team3')
		team4 = types.InlineKeyboardButton(text='Команда 4', callback_data='team4')
		team5 = types.InlineKeyboardButton(text='Команда 5', callback_data='team5')
		team6 = types.InlineKeyboardButton(text='Команда 6', callback_data='team6')
		team7 = types.InlineKeyboardButton(text='Команда 7', callback_data='team7')
		team8 = types.InlineKeyboardButton(text='Команда 8', callback_data='team8')
		team9 = types.InlineKeyboardButton(text='Команда 9', callback_data='team9')
		team10 = types.InlineKeyboardButton(text='Команда 10', callback_data='team10')
		markupInline.add(team1)
		markupInline.add(team2)
		markupInline.add(team3)
		markupInline.add(team4)
		markupInline.add(team5)
		markupInline.add(team6)
		markupInline.add(team7)
		markupInline.add(team8)
		markupInline.add(team9)
		markupInline.add(team10)
		mes_text = load_text('start_game')
		img = open('img/2.jpg', 'rb')
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
		 chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markupInline)

	elif call.data == 'start_stage':
		markupInline = types.InlineKeyboardMarkup()
		finish_stage = types.InlineKeyboardButton(text='Закончить испытание!', callback_data='finish_stage')
		markupInline.add(finish_stage)
		mes_text = load_text('start_stage')
		img = open('img/2.jpg', 'rb')
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
		 chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markupInline)

	elif call.data == 'finish_stage':
		markupInline = types.InlineKeyboardMarkup()
		keys = get_keys(call.message.chat.id)
		key1 = types.InlineKeyboardButton(text=keys[0], callback_data='key1')
		key2 = types.InlineKeyboardButton(text=keys[1], callback_data='key2')
		key3 = types.InlineKeyboardButton(text=keys[2], callback_data='key3')
		key4 = types.InlineKeyboardButton(text=keys[3], callback_data='key4')
		key_no = types.InlineKeyboardButton(text='Задание не выполнено', callback_data='key_no')
		markupInline.add(key1)
		markupInline.add(key2)
		markupInline.add(key3)
		markupInline.add(key4)
		markupInline.add(key_no)
		mes_text = load_text('key')
		img = open('img/2.jpg', 'rb')
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
		 chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markupInline)

	elif call.data == 'key1':	
		check_key(call.message.chat.id, call.message.message_id, 1)
	elif call.data == 'key2':
		check_key(call.message.chat.id, call.message.message_id, 2)
	elif call.data == 'key3':
		check_key(call.message.chat.id, call.message.message_id, 3)
	elif call.data == 'key4':
		check_key(call.message.chat.id, call.message.message_id, 4)
	elif call.data == 'key_no':
		markupInline = types.InlineKeyboardMarkup()
		next_stage = types.InlineKeyboardButton(text='Следующее задание!', callback_data='next_stage')
		restart_stage = types.InlineKeyboardButton(text='Переиграть!', callback_data='restart_stage')
		how_many_keys = types.InlineKeyboardButton(text='Сколько у меня ключей?', callback_data='how_many_keys2')
		final_game = types.InlineKeyboardButton(text='Закончить игру!', callback_data='final_game')
		markupInline.add(next_stage)
		markupInline.add(restart_stage)
		markupInline.add(how_many_keys)
		markupInline.add(final_game)
		mes_text = load_text('key_no')
		img = open('img/2.jpg', 'rb')
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
	 chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markupInline)
	elif call.data == 'key':
		markupInline = types.InlineKeyboardMarkup()
		next_stage = types.InlineKeyboardButton(text='Следующее задание!', callback_data='next_stage')
		how_many_keys = types.InlineKeyboardButton(text='Сколько у меня ключей?', callback_data='how_many_keys1')
		final_game = types.InlineKeyboardButton(text='Закончить игру!', callback_data='final_game')
		markupInline.add(next_stage)
		markupInline.add(how_many_keys)
		markupInline.add(final_game)
		mes_text = 'Что дальше?)'
		img = open('img/2.jpg', 'rb')
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
	 chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markupInline)

	elif call.data == 'next_stage':
		db.up_stage(call.message.chat.id)
		mes_text, img = get_stage_info(call.message.chat.id)
		send_road_message(call.message.chat.id, call.message.message_id, mes_text, img)

	elif call.data == 'restart_stage':
		mes_text, img = get_stage_info(call.message.chat.id)
		send_road_message(call.message.chat.id, call.message.message_id, mes_text, img)

	elif call.data == 'how_many_keys1':
		markupInline = types.InlineKeyboardMarkup()
		key = types.InlineKeyboardButton(text='Продолжить', callback_data='key')
		markupInline.add(key)
		keys = db.get_user_keys(call.message.chat.id)
		mes_text = f'У вас {keys} ключей!'
		if keys == 1:
			mes_text = f'У вас {keys} ключ!'
		elif keys < 5:
			mes_text = f'У вас {keys} ключа!'
		img = open('img/2.jpg', 'rb')
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
		 chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markupInline)

	elif call.data == 'how_many_keys2':
		markupInline = types.InlineKeyboardMarkup()
		next_stage = types.InlineKeyboardButton(text='Продолжить', callback_data='key_no')
		markupInline.add(key_no)
		keys = db.get_user_keys(call.message.chat.id)
		mes_text = f'У вас {keys} ключей!'
		if keys == 1:
			mes_text = f'У вас {keys} ключ!'
		elif keys < 5:
			mes_text = f'У вас {keys} ключа!'
		img = open('img/2.jpg', 'rb')
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
		 chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markupInline)

	elif call.data == 'final_game':
		finish_game(call.message.chat.id, call.message.message_id)

def finish_game(user_id, message_id):
	keys = db.get_user_keys(user_id)
	mes_text = load_text('finish_game')
	mes_text = mes_text.replace('N', f'{keys}')
	if keys == 1:
		mes_text = mes_text.replace('ключей', 'ключ')
	elif keys < 5 and keys != 0:
		mes_text = mes_text.replace('ключей', 'ключа')
	img = open('img/2.jpg', 'rb')
	db.del_user(user_id)
	bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
	 chat_id=user_id, message_id=message_id)

def get_stage_info(user_id):
	key_id = get_key_id(user_id)
	img = open('img/1.png', 'rb')
	return load_text(key_id), img

def check_key(user_id, message_id, key):
	markupInline = types.InlineKeyboardMarkup()
	next_stage = types.InlineKeyboardButton(text='Следующее задание!', callback_data='next_stage')
	how_many_keys = types.InlineKeyboardButton(text='Сколько у меня ключей?', callback_data='how_many_keys1')
	final_game = types.InlineKeyboardButton(text='Закончить игру!', callback_data='final_game')
	markupInline.add(next_stage)
	markupInline.add(how_many_keys)
	markupInline.add(final_game)
	if add_key(user_id, key):
		mes_text = '- Ура! Вы получили ещё 1 ключ!'
		img = open('img/2.jpg', 'rb')
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
	 chat_id=user_id, message_id=message_id, reply_markup=markupInline)
	else:
		mes_text = '- Не расстраивайтесь, но ключ вы не получите.'
		img = open('img/2.jpg', 'rb')
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
	 chat_id=user_id, message_id=message_id, reply_markup=markupInline)

def add_key(user_id, selected_key):
	key_id = get_key_id(user_id)
	key = int(db.check_key(key_id, selected_key))
	db.add_key(user_id, key)
	return key

def load_text(file_name):
	try:
		with open(f'texts/{file_name}.txt') as f:
			return f.read()
	except Exception as e:
		print(e)
		return 'Ошибочка вышла)'

def get_key_id(user_id):
	stage = db.get_stage(user_id)
	team_id = db.get_team(user_id)
	return f'{team_id}-{stage}'

def send_road_message(user_id, message_id, mes_text, img):
	if db.get_stage(user_id) < STAGES:
		markupInline = types.InlineKeyboardMarkup()
		start = types.InlineKeyboardButton(text='Начать испытание!', callback_data='start_stage')
		markupInline.add(start)
		bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
		 chat_id=user_id, message_id=message_id, reply_markup=markupInline)
	else:
		finish_game(user_id, message_id)

def send_first_road_message(user_id, message_id, team_id):
	db.set_team(user_id, team_id)
	mes_text = load_text(f'{team_id}-0')
	img = open('img/2.jpg', 'rb')
	send_road_message(user_id, message_id, mes_text, img)

def send_question_message(user_id, message_id, mes_text, img):
	markupInline = types.InlineKeyboardMarkup()
	what_is_key = types.InlineKeyboardButton(text='Что за ключи?', callback_data='what_is_key')
	how_do_tasks = types.InlineKeyboardButton(text='Как выполнять задания?', callback_data='how_do_tasks')
	how_get_keys = types.InlineKeyboardButton(text='Как зарабатываются ключи?', callback_data='how_get_keys')
	any_questions = types.InlineKeyboardButton(text='К кому обращаться в случае других вопросов?', callback_data='any_questions')
	start_game = types.InlineKeyboardButton(text='Начать игру!', callback_data='start_game')
	markupInline.add(what_is_key)
	markupInline.add(how_do_tasks)
	markupInline.add(how_get_keys)
	markupInline.add(any_questions)
	markupInline.add(start_game)
	bot.edit_message_media(media=telebot.types.InputMedia(type='photo', media=img, caption = mes_text),\
	 chat_id=user_id, message_id=message_id, reply_markup=markupInline)

def get_keys(user_id):
	stage = db.get_stage(user_id)
	team_id = db.get_team(user_id)
	return db.get_keys(f'{team_id}-{stage}')

bot.polling(non_stop="True")