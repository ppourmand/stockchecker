# Pasha Pourmand
# November 22, 2015
from yahoo_finance import Share
import time
import datetime

OPEN_HOURS = datetime.time(hour=6,minute=30)
CLOSE_HOURS = datetime.time(hour=13)

def print_stats(ticker,is_trading_hours):
  stock = Share(ticker)
  stock.refresh()
  
  if(is_trading_hours == True):
    print("Current Price:  $" + stock.get_price() + "\n--------------------------------------")
  else:
    print("Previous Close: $" + stock.get_prev_close())
    print("Opening Price:  $" + stock.get_open())
    print("Current Price:  $" + stock.get_price() + "\n--------------------------------------")


def translate_name_to_ticker(company_name):
  translation_dict = {'square':'SQ','yahoo':'YHOO',
                      'facebook':'FB','apple':"AAPL",
                      'google':'GOOG','twitter':'TWTR'}

  if(translation_dict.has_key(company_name) == False):
    print("Sorry, that company hasn't been added.\n--------------------------------------")
    return 'error'

  return translation_dict[company_name]

def main():
  while(True):
    company_name = raw_input("Company name (q to quit):").lower()

    # checking to quit
    if(company_name == 'q'):
      return

    # translation to ticker and print info
    ticker = translate_name_to_ticker(company_name)

    # grab the current time of day
    current_time = datetime.datetime.today().time()
    
    # if there is no error and stock exchanges are open
    # print just current price, otherwise print open/close as well
    if(ticker != 'error'):
      if(datetime.datetime.today().weekday() <= 4 and current_time >= OPEN_HOURS
                                                  and current_time <= CLOSE_HOURS):
        while(1):
          print_stats(ticker,True)
          time.sleep(30)
      else:
        print_stats(ticker,False)

if __name__ == "__main__":
  main()

