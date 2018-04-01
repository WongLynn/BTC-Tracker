# BTC-Tracker

![alt text](https://i.imgur.com/uiELIGR.png)

Always on top, moveable ticker that will display current Bitfinex BTC price and indicate market sentiment by setting price text color.

Sentiment is calculated by tracking increase/decrease in Bitfinex BTCUSD short/long margin positions, accuracy is work in progress, pull latest source regularly to have the most up to date sentiment definitions or fork and tweak code to your liking.

## Requirements

* Python 3.6, https://www.python.org/downloads/release/python-364/
* Autohotkey, https://autohotkey.com/download/

Download the file structure to a local folder.

Start the application by running ticker.ahk

## Usage

Move the window where you want by click/dragging on the grey top bar

Prices will be queried every 10 seconds, sentiment index will start counting from application start so will not immediately indicate current sentiment but will do after the application has been running for a while.

Price text will be grey when sentiment index is bullish/neutral, orange when medium bearish and red when bearish
