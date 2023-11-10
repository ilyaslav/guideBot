import psycopg2
import random

def exeptinons(func):
	def wrappper(*args, **kwargs):
		try:
			data = func(*args, **kwargs)
			return data
		except Exception as e:
			print(e)
	return wrappper

class Database:
	def __init__(self, dbname, user, password, host):
		self.conn = psycopg2.connect(dbname=dbname, user=user, 
                        password=password, host=host)
		self.cursor = self.conn.cursor()

	@exeptinons
	def create_tables(self):
		with self.conn:
			self.cursor.execute("\
				CREATE TABLE users(\
				user_id integer PRIMARY KEY,\
				team_id integer,\
				stage integer DEFAULT 0,\
				keys integer DEFAULT 0);")

		with self.conn:
			self.cursor.execute("\
				CREATE TABLE keys(\
				key_id varchar(8) PRIMARY KEY,\
				key1 varchar(20),\
				key2 varchar(20),\
				key3 varchar(20),\
				key4 varchar(20),\
				key_true integer);")

	@exeptinons
	def insert_keys(self):
		word_list = load_list('words')
		for i in range(1,11):
			for j in range(10):
				key1 = word_list.pop(random.randint(0,99))
				key2 = word_list.pop(random.randint(0,98))
				key3 = word_list.pop(random.randint(0,97))
				key4 = word_list.pop(random.randint(0,96))
				word_list.append(key1)
				word_list.append(key2)
				word_list.append(key3)
				word_list.append(key4)
				key_true = random.randint(1, 4)
				self.cursor.execute(f"INSERT INTO keys (key_id, key1, key2, key3, key4, key_true) VALUES\
					('{i}-{j}', '{key1}', '{key2}', '{key3}', '{key4}', {key_true})")
				self.conn.commit()

	@exeptinons
	def clear_table(self, table_name):
		with self.conn:
			self.cursor.execute(f"DELETE FROM {table_name}")

	@exeptinons
	def get_table(self, table_name):
		res = self.cursor.execute(f"SELECT * FROM {table_name}")
		return self.cursor.fetchone()

	@exeptinons
	def user_exist(self, user_id):
		result = self.cursor.execute(f"SELECT user_id FROM users WHERE user_id={user_id}")
		return bool(len(self.cursor.fetchone()))	

	@exeptinons
	def set_team(self, user_id, team_id):
		self.cursor.execute(f"UPDATE users SET team_id = {team_id} WHERE user_id={user_id}")
		self.conn.commit()

	@exeptinons
	def add_user(self, user_id):
		self.cursor.execute(f"INSERT INTO users (user_id) VALUES ({user_id})")
		self.conn.commit()

	@exeptinons
	def del_user(self, user_id):
		self.cursor.execute(f"DELETE FROM users WHERE user_id = {user_id}")
		self.conn.commit()

	@exeptinons
	def check_key(self, key_id, key):
		result = self.cursor.execute(f"SELECT * FROM keys WHERE key_id='{key_id}' AND key_true={key}")
		return bool(len(self.cursor.fetchall()))

	@exeptinons
	def up_stage(self, user_id):
		self.cursor.execute(f"UPDATE users SET stage = stage+1 WHERE user_id = {user_id}")
		self.conn.commit()

	@exeptinons
	def add_key(self, user_id, key):
		self.cursor.execute(f"UPDATE users SET keys = keys+{key} WHERE user_id = {user_id}")
		self.conn.commit()

	@exeptinons
	def get_stage(self, user_id):
		result = self.cursor.execute(f"SELECT stage FROM users WHERE user_id={user_id}")
		return self.cursor.fetchone()[0]

	@exeptinons
	def get_user_keys(self, user_id):
		result = self.cursor.execute(f"SELECT keys FROM users WHERE user_id={user_id}")
		return self.cursor.fetchone()[0]

	@exeptinons
	def get_keys(self, key_id):
		result = self.cursor.execute(f"SELECT key1, key2, key3, key4 FROM keys WHERE key_id='{key_id}'")
		return self.cursor.fetchone()

	@exeptinons
	def get_team(self, user_id):
		result = self.cursor.execute(f"SELECT team_id FROM users WHERE user_id={user_id}")
		return self.cursor.fetchone()[0]

def load_list(file_name):
	try:
		word_list = []
		with open(f'texts/{file_name}.txt') as f:
			for line in f:
				word_list.append(line[:-1])
		return word_list
	except Exception as e:
		print(e)

if __name__ == '__main__':
	#db = Database('mero2', 'postgres', '240816', 'localhost')
	#db.insert_keys()
	for i in range(1,11):
		for j in range(10):
			with open(f'texts/{i}-{j}.txt', 'w') as f:
				f.write('- Ваш ключик ожидает вас у мостика «ВЛЮБЛЕННЫХ». Не забудьте нажать «Начать испытание», когда будете на месте!')