# This is a simplified Login System for educational purposes only 
# This is not a complete system, do not count on it as-is for security

import md5
user_password_hashes = {}

def signup():
	global user_password_hashes
	print 'Welcome to our new Thing!'
	print 'Please Sign Up below:'
	username = raw_input('Username: ')
	if username in user_password_hashes:
		print 'That Username is already taken!'
		return False
	pw = raw_input('Password: ')
	pw2 = raw_input('Confirm Password: ')
	if pw == pw2:
		print 'Passwords match'
		user_password_hashes[username] = md5.md5(pw).hexdigest()
		print 'Signup complete. Welcome, ' + username + '!'
		return True
	else:
		print 'Your passwords did not match!'
		return False

def login():
	global user_password_hashes
	username = raw_input('Username: ')
	pw = raw_input('Password: ')
	if username in user_password_hashes:
		if md5.md5(pw).hexdigest() == user_password_hashes[username]:
			print 'You are now logged in as '+username
			return True
	print 'Invalid login'
	return False

