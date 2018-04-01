import requests
import json
import math
import time
import sys

from binance.client import Client

def getFinex(): # Function to get BTCUSDSHORTS and BTCUSDLONGS ticker values from Bitfinex API

	r = requests.request("GET","https://api.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:short/last")
	data = r.json()
	get_shorts = math.floor(data[1])

	time.sleep(2)


	r = requests.request("GET","https://api.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:long/last")
	data = r.json()
	get_longs = math.floor(data[1])

	time.sleep(2)

	r = requests.request("GET","https://api.bitfinex.com/v2/ticker/tBTCUSD")
	data = r.json()
	price_btc = math.floor(data[0])

	time.sleep(2)

	return (get_shorts, get_longs, price_btc)

# Intitialize variables

total_shorts_last, total_longs_last, price_btc = getFinex()
panic_index = 0

textfile_path = sys.argv[1]

while True:
	try:
		total_shorts, total_longs, price_btc = getFinex()
	except:
		continue

	# if total_shorts = 11

	if total_shorts > total_shorts_last:
		panic_index += 1
	elif total_shorts < total_shorts_last:
		panic_index -= 1
	
	if total_longs > total_longs_last:
		panic_index -= 1
	elif total_longs < total_longs_last:
		panic_index += 1

	if panic_index > 20:
		panic_index = 20
	if panic_index < 0:
		panic_index = 0	

	total_shorts_last = total_shorts
	total_longs_last = total_longs

	
	text_file = open(textfile_path, "w")
	text_file.write(str(price_btc) + "|" + str(panic_index))
	text_file.close()

	print (total_shorts, total_longs, panic_index, price_btc)

	time.sleep(4)