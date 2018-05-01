from flask import request, render_template
from flask import Response
from flask import jsonify
from ioc_server import app
from ioc_server import db
from ioc_server.models import User
import os
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

@app.route('/register', methods=['GET', 'POST'])
def register():
	return 1

@app.route('/login', methods=['GET', 'POST'])
def login():
	pass

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	pass

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
def _register():
	json_data = request.json
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

