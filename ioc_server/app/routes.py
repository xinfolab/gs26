from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
