# coding=utf-8

import random
from app import current_time, vk_api

def chooseUser():	

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
	
	
	user = chooseUser(vk_api, 'last_seen, followers_count, can_write_private_message, photo_max_orig')
	
	while not valid(user, current_time):
		user = chooseUser(vk_api, 'last_seen, followers_count, can_write_private_message, photo_max_orig')

	return user