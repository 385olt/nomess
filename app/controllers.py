# coding=utf-8

from flask import render_template, flash, redirect, g
from app import app, statistics
from .models import chooseUser, updateStatistics

@app.route('/')
@app.route('/index')
def index():
	updateStatistics()
	return render_template('index.html', statistics=statistics[:16])

@app.route('/choose')
def choose():
	return render_template('choose.html', user=chooseUser())