from flask import request
from flask import Response
from flask import render_template
from flask import jsonify
from flask import session
from ioc_server import app
from ioc_server import db
from ioc_server import bcrypt
from ioc_server.models import User
import os
import re
from werkzeug.datastructures import Headers

@app.route('/')
@app.route('/dashboard', methods=['GET'])
def dashboard():
	return render_template('dashboard.html')

@app.route('/icons', methods=['GET'])
def icons():
	return render_template('icons.html')

@app.route('/map', methods=['GET'])
def map():
	return render_template('map.html')

@app.route('/tables', methods=['GET'])
def tables():
	return render_template('tables.html')

@app.route('/upgrade', methods=['GET'])
def upgrade():
	return render_template('upgrade.html')

@app.route('/notifications', methods=['GET'])
def notifications():
	return render_template('notifications.html')

@app.route('/typography', methods=['GET'])
def typography():
	return render_template('typography.html')

@app.route('/user', methods=['GET'])
def user():
	return render_template('user.html', methods=['GET'])

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
	print(json_data['password'])
	if json_data['password'] == 'a':
		return jsonify({'result': 'password_empty'})
	elif json_data['password'] != json_data['password_confirm']:
		return jsonify({'result': 'confirm_failed'})
	elif not(re.findall("(.*\@.*\..*)", json_data['email'])):
		return jsonify({'result': 'email_failed'})

	user = User(
		email = json_data['email'],
		username = json_data['username'],
		password = json_data['password'],
		)
	try:
		db.session.add(user)
		db.session.commit()
		status = 'success'
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

@app.route('/api/logout')
def logout():
	session.pop('logged_in', None)
	return jsonify({'result': 'success'})