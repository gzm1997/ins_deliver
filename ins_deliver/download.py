from ins_deliver.user import User
from ins_deliver import args 
import os
from bs4 import BeautifulSoup
import time
from urllib.request import urlretrieve

def make_folder(User):
	folder_name = User.get_account()
	while os.path.exists(folder_name):
		folder_name = input("文件夹已存在，请输入新的数据存储文件夹名称：")
	os.makedirs(folder_name + "/pics")
	os.makedirs(folder_name + "/videos")
	return folder_name

def download(imgs, videos, User):
	img_limit = int(User.get_pic_num())
	video_limit = int(User.get_video_num())
	folder_name = make_folder(User)

	index = 0
	for img in imgs:
		if index > img_limit:
			break
		urlretrieve(img["src"], folder_name + "/pics/" + str(index) + args.img_form)
		time.sleep(0.5)
		index += 1	

	index = 0
	for video in videos:
		if index > video_limit:
			break
		urlretrieve(video["src"], folder_name + "/videos/" + str(index) + args.video_form)
		time.sleep(0.5)
		index += 1	
	print("下载完毕！")

def load_more_by_button(driver, button):
	button.click()
	driver.implicitly_wait(0.5)
	return driver

def download_content_by_url(driver, url, folder_name):
	driver.get(url)
	bObj = BeautifulSoup(driver.page_source, "html.parser")
	img = bObj.find("img", {"class": "_icyx7"})
	video = bObj.find("video", {"class": "_c8hkj"})	

	while os.path.exists(folder_name):
		folder_name = input("文件夹已存在，请重新命名：")

	if img:
		os.makedirs(folder_name + "/pics")
		urlretrieve(img["src"], folder_name + "/pics/pic" + args.img_form)
	if video:
		os.makedirs(folder_name + "/videos")
		urlretrieve(video["src"], folder_name + "/videos/video", args.video_form)
	

def download_contents_by_url(driver, url, folder_name, num_pic, num_video):
	driver.get(url)
	bObj = BeautifulSoup(driver.page_source, "html.parser")
	imgs = bObj.findAll("img", {"class": "_icyx7"})
	videos = bObj.findAll("video", {"class": "_c8hkj"})

	while os.path.exists(folder_name):
		folder_name = input("文件夹已存在，请重新命名：")

	while 1:
		if len(imgs) != 0 and len(imgs) > int(num_pic):
			os.makedirs(folder_name + "/pics")
			index = 0
			for img in imgs:
				if index > int(num_pic):
					break
				urlretrieve(img["src"], folder_name + "/pics/" + str(index) + args.img_form)
				time.sleep(0.5)	
				index += 1	
			print("图片成功保存！")
			break

		elif len(imgs) != 0 and len(imgs) < int(num_pic):
			print("图片数量不足，自动加载中...")

			button = bObj.find("a", {"class": "_8imhp"})
			if button:
				driver = load_more_by_button(driver, driver.find_element_by_class_name("_8imhp"))
				bObj = BeautifulSoup(driver.page_source, "html.parser")
				imgs = bObj.findAll("img", {"class": "_icyx7"})
				videos = bObj.findAll("video", {"class": "_c8hkj"})

			else:
				driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
				driver.implicitly_wait(0.5)

				bObj = BeautifulSoup(driver.page_source, "html.parser")
				imgs = bObj.findAll("img", {"class": "_icyx7"})
				videos = bObj.findAll("video", {"class": "_c8hkj"})

		elif len(imgs) == 0:
			print("没有图片可以下载")
			break
	while 1:
		if len(videos) != 0 and len(videos) > int(num_video):
			os.makedirs(folder_name + "/videos")
			index = 0
			for video in videos:
				if index > int(num_video):
					break
				urlretrieve(video["src"], folder_name + "/videos/" + str(index) + args.video_form)
				time.sleep(0.5)		
				index += 1	
			print("视频成功保存！")

		elif len(videos) != 0 and len(videos) < int(num_video):
			print("视频数量不足，自动加载中...")

			button = bObj.find("a", {"class": "_8imhp"})
			if button:
				driver = load_more_by_button(driver, driver.find_element_by_class_name("_8imhp"))
				bObj = BeautifulSoup(driver.page_source, "html.parser")
				videos = bObj.findAll("video", {"class": "_c8hkj"})

			else:
				driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
				driver.implicitly_wait(0.5)

				bObj = BeautifulSoup(driver.page_source)
				videos = bObj.findAll("video", {"class": "_c8hkj"})

		elif len(videos) == 0:
			print("没有视频可以下载")
			break