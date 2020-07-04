from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
import pandas as pd
import os

class StockConnect:

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.trend = ''
        # "GENERATE TOKEN HERE AND BUILD THE NECCESSARY CONNECTION TO THE API END POINT"
        # THIS FUNCTION WILL MAKE A CONNECTION TO THE API AND WON'T RETURN ANYTHING AS OF NOW
        pass

    def getStocksFromSelenium(self):
        #launch url
        url = "view-source:https://www.nseindia.com/api/market-data-pre-open?key=NIFTY"
        # create a new Firefox session
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        driver.get(url)
        html = driver.find_element_by_id('viewsource')
        
        data=json.loads(BeautifulSoup(driver.page_source).findAll(text=True)[1])
        driver.quit() # closes the browser session

        advances = data['advances'] # shows the number of stocks positive
        declines = data['declines'] # shows the number of stocks negative
        # we'll use above advances and declines to decide the trend
        self.trend = 'Bull' if advances>declines else 'Bear'
        
        return pd.DataFrame(data['data'])
        # pass

    # FUNCTION TO LIST THE STOCKS AS PER THE STRATEGY, IN THIS CASE IT'S GAPPING STOCKS
    def listStocks(self):
        # things to consider are, FUNDS AVAILABLE, PRICE RANGE OF STOCKS
        # WILL RETURN THE STOCKS LIST
        pass

    def filterStocks(self):
    	# THIS FUNCTION WILL TAKE THE LISTsTOCKS AND FILTER THEM ACCORDING TO THE CRITERIA, IN THIS CASE 5 MIN CANDLES SHOULD NOT BE MOVING IN THE OPPOSTITE DIRECTION
    	# THIS FUNCTION WILL RETURN THE N NUMBER OF SHARES AFTER FILTERING OUT (1)
        stockList = self.getStocksFromSelenium()
        filteredStocks = []
        if self.trend=='Bull':
            # MARKET IS GREEN, LET'S SEARCH FOR BUYING OPPORTUNITIES
            for row in stockList['metadata']:
                if row['pChange'] >= 2 and row['previousClose'] <= 600:
                    filteredStocks.append(row['symbol'])
        else:
            # MARKET IS RED, LET'S SEARCH FOR SELLING OPPORTUNITIES    
            for row in stockList['metadata']:
                if row['pChange'] <= -2 and row['previousClose'] <= 600:
                    filteredStocks.append(row['symbol'])

        print(filteredStocks)
    	# pass

    def monitorForSelection(self):
        # THIS IS THE FUNCTION WHICH MONITORS ALL THE ELIGIBLE STOCKS FOR TREND REVERSAL AND IF EVEYTHING LOOKS GOOD X STOCKS THEN A RANDOM STOCK IS RETURNED FOR ORDER PLACEMENT
        pass

    def placeCoverOrder(self):
    	# THIS FUNCTION WILL PLACE A COVER ORDER WITH SL % DEFINED FOR A PARTICULAR STOCK
    	# MAYBE RETURN AN ORDER ID OR SOMETHING
    	pass

    def placeEquitoOrder(self):
        pass    

    def squareOff(self):
    	# THIS WILL SQUARE OFF ANY POSTITIONS WITH THE DEFINED TARGET. MAYBE WITH ORDER ID OR SOMETHING
    	# RETURN THE STATUS I GUESS
    	pass	
	




