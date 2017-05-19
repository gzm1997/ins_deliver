import ins_deliver.args as args
from ins_deliver.user import User
import io
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def login(User):
	driver =  webdriver.PhantomJS(executable_path = args.PhantomJS_executable_path, service_args = args.service_args)
	driver.get(args.login_url)
	driver.implicitly_wait(0.5)

	a = driver.find_elements_by_tag_name("a")
	login_a = a[2]
	login_a.click()
	driver.implicitly_wait(0.5)

	account = driver.find_element_by_xpath("//input[@name='username']")
	account.clear()
	account.send_keys(User.get_account())
	print("账号输入完成!")

	passwd = driver.find_element_by_xpath("//input[@name='password']")
	passwd.clear()
	passwd.send_keys(User.get_password())
	print("密码输入完成!")

	button = driver.find_element_by_class_name("_ah57t")
	button.click()
	print("开始登陆!")	
	driver.implicitly_wait(0.5)

	bObj = BeautifulSoup(driver.page_source, "html.parser")
	img = bObj.findAll("img", {"class": "_icyx7"})	
	video = bObj.findAll("video", {"class": "_c8hkj"})

	index_pic = len(img)
	index_video = len(video)
	while index_pic < int(User.get_pic_num()) or index_video < int(User.get_video_num()):
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
		driver.implicitly_wait(0.5)

		bObj = BeautifulSoup(driver.page_source, "html.parser")
		img = bObj.findAll("img", {"class": "_icyx7"})	
		video = bObj.findAll("video", {"class": "_c8hkj"})
		index_pic = len(img)
		index_video = len(video)

	print("完成数据采集！")

	return driver, img, video



