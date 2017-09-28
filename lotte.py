import requests
import bs4


r = requests.get('http://ketqua.net')
s = r.text
lines = s.splitlines()
for line in lines:
	if 'rs_0_0' in line:
		line = line.split('rs_len="5"')[1]
		print("ket qua dac biet:", line[1:6])