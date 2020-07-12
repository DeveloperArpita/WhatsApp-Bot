from selenium import webdriver
import time
from playsound import playsound
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

name = input("Enter the Victim Name: ")
print('Scan the QR Code!')
driver = webdriver.Chrome(executable_path=r'C:\Python23\Lib\site-packages\chromedriver.exe')
driver.get('https://web.whatsapp.com')
input("Press Enter after scanning QR Code")
print('Starting Script')

var = 1
driver.find_element_by_xpath("//span[@title='{}']".format(name)).click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option']//span[@title='{}']".format(name)))).click()
while True:

	if var==1: # Searching while offline
		try:
			print('.',end='')
			time.sleep(5)
			flag = driver.find_element_by_xpath("//span[@title='online']")
			print('')
			print(time.strftime('%H:%M:%S'),end='-')
			playsound('message_tone.mp3.mp3') # playing the sound when it shows online
			time.sleep(1)
			var = 2
		except:
			pass
		
	elif var==2: # Searching while online
		try:
			flag = driver.find_element_by_xpath("//span[@title='online']")
			time.sleep(1)
		except:
			print(time.strftime('%H:%M:%S'))
			time.sleep(30)
			var = 1
