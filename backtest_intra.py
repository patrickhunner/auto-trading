import csv
import requests
import pandas as pd
import time
from os.path import exists


def historical_data_intraday(years,ticker,time_agg):
    est_time = (years * 12) / 5
    print("Estimated time is {} minutes".format(est_time))
    calls = 0
    for year in range(1,years + 1):
        for month in range(1,13):
            print(month)
            url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={}&interval={}&slice=year{}month{}&apikey=IWSS4R694TVBE5LG".format(ticker,time_agg,year,month)
            data = pd.read_csv(url)
            data.to_csv("historical_60min.csv",mode="a", index=False, header=False)
            calls += 1
            if calls == 5:
                print("sleep")
                time.sleep(60)
                calls = 0

def calc_supertrend(mult1, mult2, high, low, ticker, time):
    df = pd.read_csv("{}_{}.csv".format(time,ticker))
    atr = calc_atr()
    bas_up = ((high + low) / 2) + mult1 * atr
    bas_low = ((high + low) / 2) - mult2 * atr
    fin_up


def calc_atr():
    return 


def historical_data_daily(ticker):
    clear_csv("historical1day.csv")
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={}&datatype=csv&apikey=IWSS4R694TVBE5LG".format(ticker)
    data = pd.read_csv(url)
    data.to_csv("historical_1day.csv", mode="a", index=False)

def clear_csv(filename):
    f = open(filename, "w+")
    f.close()

# historical_data_intraday()
historical_data_daily("SPY")
# clear_csv("historical_60min.csv")
# clear_csv("historical_1day.csv")
print("success")
