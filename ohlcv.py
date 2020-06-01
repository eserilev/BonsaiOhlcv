import datetime
import ccxt


# database stuff for later
# client = pymongo.MongoClient("")
# bonsai_db = client.bonsai
# ohlcvCollection = bonsai_db.ohlcvs

# Bonsai implementation of
# open high low close and volume (ohlcv)
# data fetching and logging
class BonsaiOhlcv():
    
    def __init__(self):
        self.bitmex = ccxt.bitmex({
            'rateLimit': 10000,
            'enableRateLimit': True
        })
    
    # grab the ohlcv of bitcoin 
    # starting at from_date and 
    # ending at the current date
    # using the ccxt bitmex client
    #
    # returns: a list of ohlcv data
    def get_ohlcv(self, from_date):
        now = self.bitmex.milliseconds()
        then = from_date.timestamp() * 1000
        time_span = now - then
        return self.bitmex.fetch_ohlcv('BTC/USD', '1d', time_span)

    # todo: update our ohlcv mongodb collection with the data from ohlcv_list
    # todo: create unique constraint on datestamp to prevent duplicate data
    def update_ohlcv_logs(self, ohlcv_list):
        print(len(ohlcv_list))
        for ohlcv in ohlcv_list:
            print(ohlcv)
            #ohlcvCollection.insert_one(ohlcv)


# example usage of using the BonsaiOhlcv class
# to grab current ohlcv data and log it
def main():
    print('starting ohlcv calculations')
    date_time_str = input("input a date: YYYY-MM-DD:\n")
    date_range = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
    bonsai_ohlcv = BonsaiOhlcv()
    ohlcv_list = bonsai_ohlcv.get_ohlcv(date_range)
    bonsai_ohlcv.update_ohlcv_logs(ohlcv_list)
    
if __name__ == "__main__":
    main()
   
