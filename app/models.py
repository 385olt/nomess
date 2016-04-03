# coding=utf-8

import vk
import random
import time

def chooseUser():
	current_time = int(time.time())

	vk_session = vk.Session()
	vk_api = vk.API(vk_session, lang='ru', timeout=10)
	
	def chooseUser(vk_api, fields):
		result = vk_api.users.get(user_ids=random.randint(1, 350000000), fields=fields)
		return result[0]
	
	def valid(user, current_time):
		if 'deactivated' in user or not ('last_seen' in user and 'followers_count' in user and 'can_write_private_message' in user):
			return False
		else:
			last_seen = current_time - user['last_seen']['time'] < 3 * 84600
			followers_count = user['followers_count'] < 200
			
			return last_seen and followers_count and user['can_write_private_message']
	
	
	user = chooseUser(vk_api, 'last_seen, followers_count, can_write_private_message, photo_200')
	
	while not valid(user, current_time):
		user = chooseUser(vk_api, 'last_seen, followers_count, can_write_private_message, photo_200')

	return user