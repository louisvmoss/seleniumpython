from seleniumwire import webdriver
import time
driver = webdriver.Chrome(executable_path='C:\\Users\\Lenovo\Desktop\\seleniumpython\\chromedriver.exe')
driver.header_overrides = {
	'USER-AGENT':'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
 	'X-FORWARDED-FOR':str("146.196.123.211"),
 	'X-MSISDN':str("9898888121"),
 	'Access-Control-Allow-Credentials':'True',
 	'Access-Control-Allow-Headers':'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
 	'Access-Control-Allow-Methods':'POST, GET, OPTIONS, DELETE, PUT',
 	'Access-Control-Max-Age':'3600',
	'Cache-Control':'no-cache, must-revalidate, private',
 	'X-FRAME-OPTIONS':'SAMEORIGIN'
	}

driver.get('https://1263f4ae0ff2.trffccmpny.net/?p=4396&wid=133344&wid_hmac=a5f834b3582a801f526ed4b5d7919871')
time.sleep(10)