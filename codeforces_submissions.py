# for codeforces normalround(not for educational round)
import os,time, getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import sqlite3
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
stream = os.popen('echo $USER')
output = stream.read()
userr = output.split('\n')[0]
options.add_argument("user-data-dir=/home/" + userr + "/.config/google-chrome/Default")
def login():
	question = input("File : \t")
	driver = webdriver.Chrome("/home/" + userr + "/Documents/chromedriver",chrome_options = options)
	f1 = open("/home/kartik/4thsem/forces/" + question + ".cpp", "w+")
	var = '/home/kartik/4thsem/forces/' + question + '.cpp'
	os.system('subl ' + var)
	input("")
	driver.get("https://codeforces.com/")
	# print("https://codeforces.com/contest/" + question[:-1] + "/problem/" + question[-1:])
	driver.get("https://codeforces.com/contest/" + question[:-1] + "/problem/" + question[-1:])

	# time.sleep(1)
	# driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/a[1]").click()
	# Handle = str(input("Handle/Email : \t"))
	# Pass = getpass.getpass(prompt="Password : \t")
	# time.sleep(2)
	# driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div/div/div/form/table/tbody/tr[1]/td[2]/input").send_keys(Handle)
	# driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div/div/div/form/table/tbody/tr[2]/td[2]/input").send_keys(Pass)
	# driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div/div/div/form/table/tbody/tr[4]/td/div[1]/input").click()
	# time.sleep(2)
	# driver.get("https://codeforces.com/contest/1328/")
	#driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[2]/form/table/tbody/tr[1]/td[2]/label/select/option[3]").click()
	# question = input("File : \t")
	# print(question)
	dropFileArea = driver.find_element_by_xpath("//input[@name='sourceFile']")
	dropFileArea.send_keys("/home/kartik/4thsem/forces/" + question + ".cpp")
	driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[1]/div[5]/div[4]/form/table/tbody/tr[4]/td/div/div/input").click()
	# driver.get("https://codeforces.com/contest/" + question[:-1] + "/my")

	# array = ""
	# time.sleep(3)
	# try:
	# 	array = driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[6]/a/span").text
	# except:
	# 	array = driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[6]/span").text
	# print(array)
	# while True:
	# 	time.sleep(2)
	# 	try:
	# 		array = driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[6]/a/span").text
	# 	except:
	# 		try:
	# 			array = driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[6]/span").text
	# 		except:
	# 			array = driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[6]/a").text
	# 	if(array == "Accepted" or array.find("error") == 1 or array.find("Wrong") == 1):
	# 		break

# /html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[6]/a
# /html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[6]/a/span
		# /html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr[2]/td[6]/span
	# 	driver.refresh()
	# print(array)
	driver.close()
	# time.sleep(1)
	# driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[5]/ul/li[3]/a").click()
	# driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[1]/div/div[4]/div[1]/<a href=""></a>").click()
login()
