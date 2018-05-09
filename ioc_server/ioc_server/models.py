import datetime
from hashlib import md5
from ioc_server import db, bcrypt


class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(255), unique=True, nullable=False)
	username = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)
	token = db.Column(db.String(255), nullable=False)
	admin = db.Column(db.Boolean, nullable=False, default=False)

	def __init__(self, email, username, password, admin=False):
		temp_token = '@'+email+'!'+username+'#'
		temp_token.replace('\r\n', '')
		self.email = email
		self.username = username
		self.password = bcrypt.generate_password_hash(password)
		self.token = md5(temp_token.encode('utf-8')).hexdigest()
		self.registered_on = datetime.datetime.now()
		self.admin = admin

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	def get_token(self):
		return self.token

	def __repr__(self):
		return '<User {0}>'.format(self.email)