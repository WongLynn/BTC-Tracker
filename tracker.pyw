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

	return (get_shorts, get_longs)

# Intitialize variables

total_shorts_last, total_longs_last = getFinex()
panic_index = 0

# Connect to Binance API

client = Client("", "")

textfile_path = sys.argv[1]

while True:
	try:
		total_shorts, total_longs = getFinex()
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

	infoBTC = client.get_ticker(symbol="BTCUSDT")
	priceBTC = float(infoBTC.get("askPrice"))
	priceBTC = math.floor(priceBTC)
	text_file = open(textfile_path, "w")
	text_file.write(str(priceBTC) + "|" + str(panic_index))
	text_file.close()

	print (total_shorts, total_longs, panic_index, priceBTC)

	time.sleep(8)