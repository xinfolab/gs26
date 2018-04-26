from flask import Flask, request, render_template

from flask import Response
from flask import jsonify

import os
from werkzeug.datastructures import Headers

UPDATE_FOLDER = 'update'
UPLOAD_FOLDER = 'upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/icons')
def icons():
	return render_template('icons.html')

@app.route('/map')
def map():
	return render_template('map.html')

@app.route('/tables')
def tables():
	return render_template('tables.html')

@app.route('/upgrade')
def upgrade():
	return render_template('upgrade.html')

@app.route('/notifications')
def notifications():
	return render_template('notifications.html')

@app.route('/typography')
def typography():
	return render_template('typography.html')

@app.route('/user')
def user():
	return render_template('user.html')

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
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
