# coding=utf-8

from flask import render_template, flash, redirect, g
from app import app
from .models import chooseUser

@app.route('/')
@app.route('/index')
def index():
	
	return render_template('index.html')

@app.route('/choose')
def choose():
	return render_template('choose.html', user=chooseUser())