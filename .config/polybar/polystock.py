#!/usr/bin/env python3

"""
Polystock
Author: Ashar Latif
Date: 2021-05-19
Description: A ticker displayer for polybar.
Displays the days highest gainer, biggest loser,
top crypto or any custom stock ticker.
Contact: ashar.k.latif@gmail.com
"""

from yahoo_fin import stock_info as si
from datetime import datetime
from datetime import time
import argparse

import symbols

debug = False

# How many decimal place to show in stock price.
roundNumber = 2

# Market Status Indicators
PREMARKET = 1
POSTMARKET = 3
MARKET_OPEN = 2
MARKET_CLOSED = 0

# Color Indicators
RED = '\033[31m]'
GREEN = '\033[32m]'

# Market Times
premarket_open = time(4,0)
market_open = time(9,30)
market_close = time(16,0)
postmarket_close = time(20,0)


def biggestloser():
    """Returns: stock with the the biggest losses in a given day and
    its stock price with format: 'TICKER': 'PRICE'."""

    day_losers = si.get_day_losers()
    output = str(day_losers.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(day_losers.at[0, 'Symbol']), roundNumber))
    return output

def biggestgainer():
    """Returns: stock with the biggest gains in a given day and
    its stock price with format: 'TICKER': 'PRICE'."""

    day_gainer = si.get_day_gainers()
    output = str(day_gainer.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(day_gainer.at[0, 'Symbol']), roundNumber))
    return output

def mostactive():
    """Returns: stock with the most activity in a given day and
    its stock price with format: 'TICKER': 'PRICE'."""

    day_active = si.get_day_most_active()
    output = str(day_active.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(day_active.at[0, 'Symbol']), roundNumber))
    return output

def topcrypto():
    """Returns: cryptocurrency with the highest price in a given day and its name
    with format: 'CRYPTO': 'PRICE'."""

    top_crypto = si.get_top_crypto()
    output = str(top_crypto.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(top_crypto.at[0, 'Symbol']), roundNumber))
    return output

def is_trading_hours():
    """Returns: Status of North American markets"""

    now = datetime.now().time()
    day = datetime.now().weekday()
    if day in range (0,5):
        if ((now >= premarket_open) and (now < market_open)):
            market_status = PREMARKET
        elif ((now >= market_open) and (now < market_close)):
            market_status = MARKET_OPEN
        elif ((now >= market_close) and (now < postmarket_close)):
            market_status = POSTMARKET
        else:
            market_status = MARKET_CLOSED
    else:
        market_status = MARKET_CLOSED
    return market_status

def gain_loss(ticker, today):
    now = datetime.now()
    start = now.strftime("%m") + '/' + str(int(now.strftime("%d")) - 1) + '/' + now.strftime("%Y")
    yesterday = si.get_data(ticker, start_date = start).iloc[0]['close']
    percentage = round(((100 * today) / yesterday) - 100, 2)
    if percentage > 0:
        direction = '%{F#05fc15}▲%{F-}'
    elif percentage < 0:
        direction = '%{F#fc0511}▼%{F-}'
    return direction, percentage

def customticker(ticker):
    """Returns: stock price and ticker of a stock with format 'TICKER': 'PRICE'.
    Parameter: the ticker to get a stock price on and to display.
    Precondition: ticker is a string."""
    now = datetime.now()
    output = RED + ticker + ': ' + GREEN + str(round(tickerPriceToday, roundNumber)) + percentage + '%'
    return output

def ticker_parse(dictionary):
    """Returns: stock price and ticker of a stock with format 'TICKER': 'PRICE'.
    Parameter: the ticker to get a stock price on and to display.
    Precondition: ticker is a string."""
    now = datetime.now()
    stocks = ""

    for key in dictionary:
        if dictionary[key]["type"] != "stocks":
            tickerPrice = si.get_live_price(dictionary[key]["ticker"])
        elif dictionary[key]["type"] == "stocks":
            if is_trading_hours() == PREMARKET:
                tickerPrice = si.get_premarket_price(dictionary[key]["ticker"])
                market_status = "PRE"
            elif is_trading_hours() == POSTMARKET:
                tickerPrice = si.get_postmarket_price(dictionary[key]["ticker"])
                market_status = "POST"
            else:
                tickerPrice = si.get_live_price(dictionary[key]["ticker"])
                market_status = "OPEN"
        direction, percentage = gain_loss(dictionary[key]["ticker"], tickerPrice)
        key = str('%{F#05fc15}' + key + '%{F-}')
        output = key + ': '  + str(round(tickerPrice, roundNumber)) + ' ' + direction + str(percentage) + '%' + ' | '
        stocks += output
    stocks += market_status
    return stocks

def addArguments():
    """Adds arguments from ArgParse and parses them to handle arguments"""

    parser = argparse.ArgumentParser(description='Displays stock prices outputted in a simplified form for polybar.',
                                     epilog='Output will always be in the format of: Biggest Loser, Biggest Gainer, Most Active, Top Crypto, Custom Ticker')

    # add arguments to be called
    parser.add_argument('--biggestloser', help='Prints the stock with the biggest drop in a given day.', action='store_true')
    parser.add_argument('--biggestgainer', help='Prints the stock with the biggest gain in a given day.', action='store_true')
    parser.add_argument('--mostactive', help='Prints the most active stock in a given day.', action='store_true')
    parser.add_argument('--topcrypto', help='Prints the top cryptocurrency by market cap in a given day.', action='store_true')
    parser.add_argument('--customticker', help='Display the price of a custom ticker.', type=str)
    parser.add_argument('--mytickers', help='Display the price of my tickers.', action='store_true')
    parser.add_argument('--getgroup', help='Display the price of major crypto assets.', action='store_true')

    args = parser.parse_args()

    stocks = ""

    try:
        # parse arguments
        if args.biggestloser:
            stocks += " " + biggestloser() + " "
        if args.biggestgainer:
            stocks += " " + biggestgainer() + " "
        if args.mostactive:
            stocks += " " + mostactive() + " "
        if args.topcrypto:
            stocks += " " + topcrypto() + " "
        if args.customticker:
            stocks += " " + customticker(args.customticker) + " "
        if args.mytickers:
            stocks += " " + customticker("GME") + " "
        if args.getgroup:
            stocks += ticker_parse(symbols.SYMBOLS)

    except:
        stocks = " "

    if stocks == "":
        print("You must choose a stock to be displayed! Use --help for more details...")
    else:
        print(stocks)

if __name__ == '__main__':
    addArguments()
