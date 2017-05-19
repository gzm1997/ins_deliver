class User(object):
	"""docstring for user"""
	def __init__(self, account, password, pic_num = 20, video_num = 10):
		self._account = account
		self._password = password
		self._pic_num = pic_num
		self._video_num = video_num
	def get_account(self):
		return self._account
	def get_password(self):
		return self._password
	def get_pic_num(self):
		return self._pic_num
	def get_video_num(self):
		return self._video_num


if __name__ == "__main__":
	test = User("gzm", "1234", 50, 10)
	print("account is:", test.get_account())
	print("password is:", test.get_password())
	print("pic:", test.get_pic_num())
	print("video:", test.get_video_num())

