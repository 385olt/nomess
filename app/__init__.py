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

statistics = pickle.load(open('data.dat', 'rb'))
statistics.sort(key=lambda x: x["data"]["count"], reverse=True)

app = Flask(__name__)
app.config.from_object('config')

from app import controllers, models