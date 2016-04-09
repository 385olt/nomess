# coding=utf-8

import os
from flask import Flask
from config import basedir

import time
import pickle
import vk

current_time = int(time.time())

vk_session = vk.Session()
vk_api = vk.API(vk_session, lang='ru', timeout=10)

statistics = list()
last_post_id = -1;
def loadStatistics():
	global statistics
	global last_post_id

	statistics = pickle.load(open(os.path.join(basedir, 'data.dat'), 'rb'))
	last_post_id = statistics[0]
	
	statistics = statistics[1:]
	for i, stat in enumerate(statistics):
		statistics[i]['data']['points'] = round(stat['data']['count'] + 0.1 * stat['data']['likes_count'], 1)
	statistics.sort(key=lambda x: x["data"]["points"], reverse=True)

loadStatistics()

app = Flask(__name__)
app.config.from_object('config')

from app import controllers, models