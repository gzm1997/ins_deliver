from ins_deliver.user import User
import ins_deliver.download
import ins_deliver.login
import getpass

class ins_deliver(object):
	"""docstring for ins_deliver"""
	def __init__(self):
		pass
	def register(self):
		account = input("请输入你的Instagram账号：")
		password = getpass.getpass("请输入你的Instagram密码：")
		img_limit = input("请输入需要下载的图片数量(按照ins上的排序)：")
		video_limit = input("请输入需要下载的视频数量(按照ins上的排序)：")
		self._user = User(account, password, img_limit, video_limit)

	def run(self):
		try:
			self._user
		except NameError:
			print("请完成注册！")
		else:
			self._driver, self._imgs, self._videos = login.login(self._user)

	def deliver(self):
		try:
			self._imgs
			self._videos
		except NameError:
			print("请完成运行！")
		else:
			download.download(self._imgs, self._videos, self._user)


		
		