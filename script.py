## webscraping modules
import bs4
import requests
from bs4 import BeautifulSoup


#Mysql Modules
import datetime as dt
from time import sleep
import mysql.connector

# Here are my abstracted webscraping functionss

def priceGrab(stock_tick):
    
    stock_tick = str(stock_tick)
    
    url = str('https://finance.yahoo.com/quote/'+stock_tick+'?p='+stock_tick+'&.tsrc=fin-srch')
    url= requests.get(url)
    soup=bs4.BeautifulSoup(url.text,"lxml")
    
    #find the specific html element
    price = soup.find_all('div', {'class' :'D(ib) Mend(20px)'})[0].find('span').text
    
    return price

def priceChange(stock_tick):
    
    stock_tick = str(stock_tick)
    
    url = str('https://finance.yahoo.com/quote/'+stock_tick+'?p='+stock_tick+'&.tsrc=fin-srch')
    url= requests.get(url)
    soup=bs4.BeautifulSoup(url.text,"lxml")
    
    #find the specific html element
    text = soup.find('div', {'class' :'D(ib) Mend(20px)'}).find_all('span')[1].text
    price_change = text.split(' ')[0]
    return price_change

def percentChange(stock_tick):
    
    stock_tick = str(stock_tick)
    
    url = str('https://finance.yahoo.com/quote/'+stock_tick+'?p='+stock_tick+'&.tsrc=fin-srch')
    url= requests.get(url)
    soup=bs4.BeautifulSoup(url.text,"lxml")
    
    #find the specific html element
    text = soup.find('div', {'class' :'D(ib) Mend(20px)'}).find_all('span')[1].text
    percent_change = text.split(' ')[1]
    percent_change = percent_change[1:-1]
    return percent_change


#These are my functions on the actual portfolio

def port_totalValue(portfolio):
    tv = 0
    for i in portfolio:
        tv+= i.total_value()    
    return tv    

def port_totalChange(portfolio):
    tc = 0
    for i in portfolio:
        tc += i.total_price_change()
    return round(tc,2) 


#Defining a class for each stock

class Stock:
    #Creating the init function to grab the ticker and share amount and store them as self.variables
    def __init__(self,ticker,shares):
        self.ticker = ticker
        self.shares = shares
    
    
    
    #Methods for the stock object
    
    #return the current price
    def total_value(self):
        
        # use abstracted price grab
        val = priceGrab(self.ticker)
        #remplacing commas so I can have a datatype float for the DB
        val= val.replace(',','')
        #conversion
        val = float(val)
        
        total = val * self.shares
        
        return round(total,2)
    

    def total_price_change(self):
        val = priceChange(self.ticker)
        val = float(val)
        
        val = val * self.shares
        return round(val,2)
    
    def current_percent_change(self):
        val = percentChange(self.ticker)
        val= val.replace(',','')
        val= val.replace('%','')
        
        val = round(float(val),2)
        return val
    

# definitions of the stock in my portfolio1 

port1 = {}           #portfolio def  
port1['ID'] = 1      #defining the portfolio as portfolio 1   

# defining the stocks instances in this specific portfolio
y = Stock('NVDA',1)       
x = Stock('AYX',5)
z = Stock('BLMN',40)
r = Stock('MGM',31)

port1['stocks']= [y,x,z,r]   #storing list of stock class



# The Daily Run of The Application

while True:
    
    # controlling to run on only weekdays
    if dt.date.today().isoweekday()  in [1,2,3,4,5]:
    
        # establishing the connection

        db_connection = mysql.connector.connect(
            host="localhost",
            user="danny",
            passwd="Seventy4",
            database="stock"
            )
        db_cursor = db_connection.cursor() 
        
        date = str(dt.date.today())
        
        # inputting in each individual stock for the specific portfolio
        
        for stock in port1['stocks']:
            print('PortID: {}, Ticker: {}, Shares: {}, Total_value: {}'.format(port1['ID'], stock.ticker, stock.shares, stock.total_value()))
    
            iter_query = "INSERT INTO `portfolios` (`port_ID`, `ticker`, `shares_owned`,`close_price`,`day_change`,`day_percent_change`,`date`) VALUES ('"+port1['ID']+"', '"+stock.ticker+ "', '"+stock.shares+"'', '"+stock.total_value()+"'', '"+stock.total_price_change()+"'', '"+stock.current_percent_change()+"'', '"+date+"');"
            db_cursor.execute(iter_query)
            db_connection.commit()
        
        print(indivudual stocks added)
            
        #Getting total value, totalchange and the current date
        total_port_value = str(port_totalValue(portfolio))
        total_port_change = str(port_totalChange(portfolio))
        
        query = "INSERT INTO `total` (`day`, `total_value`, `total_change`) VALUES ('"+date+"', '"+total_port_value+ "', '"+total_port_change+"');"
    
        db_cursor.execute(query)
        db_connection.commit()
        
        print(db_cursor.rowcount,"rows inserted for total port value")
       
        
    else:
        continue
    







