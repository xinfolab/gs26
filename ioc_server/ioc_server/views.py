from flask import request
from flask import Response
from flask import render_template
from flask import jsonify
from flask import session
from flask import redirect
from ioc_server import app
from ioc_server import db
from ioc_server import bcrypt
from ioc_server.models import User
import os
import re
from werkzeug.datastructures import Headers

@app.route('/')
@app.route('/signin', methods=['GET'])
def signin():
	try:
		if session['logged_in'] == True:
			return redirect('/report', code=302)
		return render_template('signin.html')
	except:
		return render_template('signin.html')

@app.route('/report', methods=['GET'])
def report():
	try:
		if session['logged_in'] == False:
			return redirect('/signin', code=302)
		return render_template('report.html')
	except:
		return render_template('signin.html')

@app.route('/icons', methods=['GET'])
def icons():
	try:
		if session['logged_in'] == False:
			return redirect('/signin', code=302)
		return render_template('icons.html')
	except:
		return render_template('signin.html')

@app.route('/map', methods=['GET'])
def map():
	try:
		if session['logged_in'] == False:
			return redirect('/signin', code=302)
		return render_template('map.html')
	except:
		return render_template('signin.html')

@app.route('/tables', methods=['GET'])
def tables():
	try:
		if session['logged_in'] == False:
			return redirect('/signin', code=302)
		return render_template('tables.html')
	except:
		return render_template('signin.html')

@app.route('/upgrade', methods=['GET'])
def upgrade():
	return render_template('upgrade.html')

@app.route('/notice', methods=['GET'])
def notice():
	try:
		if session['logged_in'] == False:
			return redirect('/signin', code=302)
		return render_template('notice.html')
	except:
		return render_template('signin.html')

@app.route('/typography', methods=['GET'])
def typography():
	try:
		if session['logged_in'] == False:
			return redirect('/signin', code=302)
		return render_template('typography.html')
	except:
		return render_template('signin.html')

@app.route('/signup', methods=['GET'])
def signup():
	return render_template('signup.html')

@app.route('/reports/<report>', methods=['POST'])
def get_report(report):
	content = request.get_json()

	path = os.path.join(os.getcwd(),'report', report)
	with open(path,'w') as f:
		f.write(str(content))

	result = 'false'
	if os.path.exists(path) == True:
		result = 'sucess'

	return jsonify({"result" : result})


@app.route('/update/<filename>', methods=['GET'])
def download_file(filename):
	files = filename.encode('utf-8')
	full_path = os.path.join('update',filename)
	headers = Headers()
	headers.add('Content-Disposition', 'attachment', filename=files)
	headers['Content-Length']= os.path.getsize(full_path)

	download_obj = open(full_path,'rb')
	
	def generate():
		for block in iter(lambda: download_obj.read(4096), b''):
			yield block
		download_obj.close()

	return Response(generate(), mimetype = 'application/octer-stream', headers=headers)
	
@app.route('/api/register', methods=['POST'])
def register():
	json_data = request.json
	if json_data['password'] == '':
		return jsonify({'result': 'password is empty'})
	elif json_data['password'] != json_data['password_confirm']:
		return jsonify({'result': 'please check password_confirm'})
	uname = User.query.filter_by(username=json_data['username']).first()
	if uname:
		return jsonify({'result': 'username duplicated'})

	user = User(
		email = json_data['email'],
		username = json_data['username'],
		password = json_data['password'],
		)
	try:
		db.session.add(user)
		db.session.commit()
		status = 'success'
		print('success')
	except:
		status = 'this user is already registerd'
	db.session.close()
	return jsonify({'result': status})

@app.route('/api/login', methods=['POST'])
def login():
	json_data = request.json
	user = User.query.filter_by(email=json_data['email']).first()
	if user and bcrypt.check_password_hash(user.password, json_data['password']):
		session['logged_in'] = True
		status = True
	else:
		status = False
	return jsonify({'result': status})

@app.route('/api/logout', methods=['GET'])
def logout():
	session.pop('logged_in', None)
	return jsonify({'result': 'success'})

@app.route('/api/status', methods=['GET'])
def status():
	try:
	    if session.get('logged_in'):
	        if session['logged_in']:
	            return jsonify({'status': True})
	    else:
	        return jsonify({'status': False})
	except:
		return jsonify({'status': False})