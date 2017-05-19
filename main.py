from ins_deliver import ins_deliver as ins
from ins_deliver.download import download_contents_by_url, download_content_by_url
from selenium import webdriver

if __name__ == "__main__":
	myins = ins()
	myins.register()
	myins.run()
	myins.deliver()


	url = input("请输入某单个ins内容页面的url进行图片和者视频下载：")
	folder_name = input("请输入下载数据保存的文件夹名称：")
	num_pic = input("请输入要下载的图片数量：")
	num_video = input("请输入要下载的视频数量：")
	url = "https://www.instagram.com/shaq/"
	download_contents_by_url(driver, url, folder_name, num_pic, num_video)

	download_content_by_url(driver, "https://www.instagram.com/p/BULc74EAN7K/", "大鲨鱼的一条ins")


