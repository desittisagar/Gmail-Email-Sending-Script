# Modules to be imported.

import time
import smtplib
from email import encoders
from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()

from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from selenium.webdriver.common.keys import Key 							# The Key class provide keys in the keyboard
from email.mime.multipart import MIMEMultipart




# Your login details.

user_name = input("Enter your user_name: ")							#prompt to input username
passwd = input("Enter your password: ")								#prompt to input password
to_email = input("Enter the sending/TO email id: ")					#prompt to input to_email address
subject = input("Enter subject: ")									#prompt to input subject
msg = input("Enter the message you want to send: ")					#prompt to input message to be sent

# Browser : Firefox.
#driver = webdriver.Chrome() for Chrome browser or
	
url = "http://www.gmail.com"										#gmail url
driver = webdriver.Firefox()										#selenium.webdriver module provides all the WebDriver implementations
driver.get(url)														#driver.get method will navigate to a page given by the URL
time.sleep(2)														#sleep for 2 seconds


# GMAIL login.
try:
	username=driver.find_element_by_name("identifier")				#Searching the element by name
	username.send_keys(user_name)									#we are sending keys
	time.sleep(2)

	next=driver.find_element_by_id("identifierNext")				#Searching the element by id
	next.click()													#clicking the button
	time.sleep(2)			

	password=driver.find_element_by_name("password")				#Searching the element by name
	password.send_keys(passwd)
	time.sleep(2)

	next=driver.find_element_by_id("passwordNext")					#Searching the element by id
	next.click()
	time.sleep(10)													#sleep for 10 seconds

	compose=driver.find_element_by_xpath("//div[@class='T-I T-I-KE L3']")		#Searching the element by xpath
	compose.click()
	time.sleep(2)

	to=driver.find_element_by_css_selector("textarea[name='to']")				#Searching the element by css selector
	to.send_keys(to_email)
	time.sleep(2)

	subj=driver.find_element_by_name("subjectbox")								#Searching the element by name
	subj.send_keys(subject)
	time.sleep(2)

	# message
	mess=driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']")		#Searching the element by xpath
	mess.send_keys(msg)
	time.sleep(2)

	send_=driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")		#Searching the element by xpath
	send_.click()
	time.sleep(2)

except Exception as e:													# enters into except if try encoutered error
	print(e)
	print("Google somewhere blocked you from login")
	print("1. Please allow local secure apps in gmail")
	print("2. Please allow third party apps")
	print("3. Please login to the browser and sync on")

driver.quit()