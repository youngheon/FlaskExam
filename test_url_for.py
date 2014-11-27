# -*- coding: utf-8 -*-
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/hello/')
def hello():
	return 'Hello Flask!'

@app.route('/profile/',methods=['POST','GET'])
def profile(username=None):
	error = None
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		if not username and not email:
				return add_profile(request.form)
	else:
		error = 'Invalid username or email'
	return  render_template('profile.html',error=error)

@app.route('/profile/<username>')
def get_profile(username):
	return 'profile : ' + username

if __name__=='__main__':
	app.run()
with app.test_request_context():
	print url_for('hello')
	print url_for('get_profile',username='flask')


#쿠키와 세션
@app.route('/')
def index():
	username=request.cookies.get('username')

@app.route('/')
def index():
	resp = make_respone(render_template('hello.html'))
	resp.set_cookie('username','flask')
	return resp

#/static/style.css
url_for('static',filename='style.css')
