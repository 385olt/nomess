# coding=utf-8

import random
import pickle
from app import current_time, vk_api, loadStatistics, statistics, last_post_id, path

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

def updateStatistics():

	# Statistics list -> dict
	statistics_dict = dict()
	for stat in statistics:
		statistics_dict[stat['uid']] = stat['data']
	
	# Get last 100 posts
	posts = vk_api.wall.get(owner_id=-115191226, count=100)

	# Update statistics dict
	i = 1
	while posts[i]['id'] != last_post_id and i < len(posts):
		if 'signer_id' in posts[i]:
			if not (posts[i]['signer_id'] in statistics_dict):
				# Add new user in statistics if new
				statistics_dict[posts[i]['signer_id']] = dict()
				statistics_dict[posts[i]['signer_id']]['count'] = 0
				statistics_dict[posts[i]['signer_id']]['likes_count'] = 0

				# Get users profile data
				profile = vk_api.users.get(user_ids=posts[i]['signer_id'], fields="photo_50")
				statistics_dict[posts[i]['signer_id']]['first_name'] = profile[0]['first_name']
				statistics_dict[posts[i]['signer_id']]['last_name'] = profile[0]['last_name']
				statistics_dict[posts[i]['signer_id']]['photo_50'] = profile[0]['photo_50']

			# Update data
			statistics_dict[posts[i]['signer_id']]['count'] += 1
			statistics_dict[posts[i]['signer_id']]['likes_count'] += posts[i]['likes']['count']

	# Statistics dict -> list
	statistics_list = list()
	statistics_list.append(posts[1]['id'])
	for uid in statistics_dict:
		statistics_list.append({'uid': uid, 'data': statistics_dict[uid]})
	
	# Write to the file
	file = open(path + 'data.dat', 'wb')
	pickle.dump(statistics_list, file)

	loadStatistics()

