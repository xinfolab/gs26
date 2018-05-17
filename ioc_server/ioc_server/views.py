from flask import request
from flask import Response
from flask import render_template
from flask import jsonify
from flask import session
from flask import redirect
from flask import abort
from flask import send_from_directory
from ioc_server import app
from ioc_server import db
from ioc_server import bcrypt
from ioc_server.models import User
from werkzeug.datastructures import Headers
import os
import re
import json


@app.route('/')
def main():
	return render_template('main.html')

@app.route('/signin', methods=['GET'])
def signin():
	try:
		if session['logged_in'] == True:
			return redirect('/report', code=302)
		return render_template('signin.html')
	except:
		return render_template('signin.html')

@app.route('/download', methods=['GET'])
def download():
	try:
		if session['logged_in'] == False:
			return redirect('/signin', code=302)
		return render_template('download.html')
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

@app.route('/contact', methods=['GET'])
def contact():
	return render_template('contact.html')

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
	try:
		if session['logged_in'] == True:
			return redirect('/report', code=302)
		return render_template('signup.html')
	except:
		return render_template('signup.html')

@app.route('/reports/<upload_time>', methods=['POST'])
def get_report(upload_time):
	json_data = request.json
	parsed_data = json.loads(json_data)
	user = User.query.filter_by(email=parsed_data['user']).first()
	path = os.path.join(app.config['REPORT_SAVE_DIRECTORY'], user.token+'/'+upload_time)
	with open(path,'w') as f:
		f.write(str(json_data))

	result = 'false'
	if os.path.exists(path) == True:
		result = 'sucess'

	return jsonify({"result" : result})

@app.route('/update/all_file_list', methods=['GET'])
def update_file_list():
	filenames = os.listdir(app.config['IOC_DOWNLOAD_DIRECTORY'])

	return str(filenames)

@app.route('/update/<filename>', methods=['GET'])
def download_file(filename):
	files = filename.encode('utf-8')
	full_path = os.path.join(app.config['IOC_DOWNLOAD_DIRECTORY'],filename)
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
		os.mkdir(os.path.join(app.config['REPORT_SAVE_DIRECTORY'], user.get_token()))
	except Exception as e:
		print(e)
		status = 'this user is already registerd'
	db.session.close()
	return jsonify({'result': status})

@app.route('/api/login', methods=['POST'])
def login():
	json_data = request.json
	user = User.query.filter_by(email=json_data['email']).first()
	if user and bcrypt.check_password_hash(user.password, json_data['password']):
		session.permanent = True
		session['logged_in'] = True
		session['user'] = user.username
		if json_data['client']:
			status = user.token
		else:
			status = True
	else:
		status = False
	return jsonify({'result': status})

@app.route('/api/logout', methods=['GET'])
def logout():
	session.pop('logged_in', None)
	session.pop('user', None)
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

@app.route('/api/download', methods=['GET'])
def downloadclient():
	return send_from_directory(app.config['CLIENT_FOLDER'],'testfile.exe')

@app.route('/api/username', methods=['GET'])
def username():
	try:
		if session.get('logged_in'):
			if session['logged_in']:
				return jsonify({'username': session['user']})
		else:
			return jsonify({'username': False})
	except:
		return jsonify({'username': False})

@app.route('/report', methods=['GET', 'POST'])
def report():
	try:
		json_data = request.json
	except Exception as e:
		json_data = None

	if json_data is None:
		try:
			if session['logged_in'] == False:
				return redirect('/signin', code=302)

			report_name = parsing('name')
			if report_name == []:
				report_data = [[],[],[],[],[]]
			else:
				report_data = parsing('data', report_name[0])
				report_count = parsing('count')

			#debug
			print(report_count)
			return render_template('report.html', report_name=report_name, report_data=report_data, report_count=report_count)
		except:
			return render_template('signin.html')
	else:
		try:
			user = User.query.filter_by(token=json_data['token']).first()
			if user:
				session['logged_in'] = True
				session['user'] = user.username
				return render_template('report.html')
		except:
			return render_template('signin.html')

@app.route('/report/<specific_name>', methods=['GET'])
def reportview(specific_name):
	report_name = parsing('name')
	report_data = parsing('data', specific_name)
	report_count = parsing('count')
	return render_template('report.html', report_name=report_name, report_data=report_data, report_count=report_count)

def getreport(report_dir, parsing_name):
	file_result = []
	proc_result = []
	ip_result = []
	reg_result = []
	count = 0
	result = []

	with open(os.path.join(report_dir, parsing_name)) as f:
		data = f.readline()
	data = json.loads(data)
	del data['user']

	for key, value in data['report']['file'].items():
		temp = [key, value]
		file_result.append(temp)
		count += 1

	for key, value in data['report']['process'].items():
		temp = [key, value]
		proc_result.append(temp)
		count += 1

	for i in data['report']['ip']:
		ip_result.append(i)
		count += 1

	for i in data['report']['registry']:
		reg_result.append(i)
		count += 1

	result.append(file_result)
	result.append(proc_result)
	result.append(ip_result)
	result.append(reg_result)
	result.append(count)
	return result

def getcount(report_dir, report_list):
	count = []
	for i in range(len(report_list)):
		with open(os.path.join(report_dir, report_list[i])) as f:
			data = f.readline()
		data = json.loads(data)
		count.append(len(data['report']['file']))
		count[i] += len(data['report']['process'])
		count[i] += len(data['report']['ip'])
		count[i] += len(data['report']['registry'])

	return count

#report[file, registry, ip, process,], user

def parsing(classification, parsing_name = None):
	try:
		username = session['user']
		user = User.query.filter_by(username=username).first()
		report_dir = os.path.join(app.config['REPORT_SAVE_DIRECTORY'],user.token)
		report_list = os.listdir(report_dir)
		if classification == 'name':
			return report_list[::-1]
		elif classification == 'data':
			report_result = getreport(report_dir, parsing_name)
			return report_result
		elif classification == 'count':
			report_count = getcount(report_dir, report_list)
			return report_count

		
	except Exception as e:
		print(e)