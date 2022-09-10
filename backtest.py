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

def historical_data_daily():
    est_time = (years) / 5
    print("Estimated time is {} minutes".format(est_time))
    calls = 0
    for year in range(1,years + 1):
        print(year)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&apikey=IWSS4R694TVBE5LG"
        data = pd.read_json(url)
        data.to_csv("historical_1day.csv", mode="a", index=False, header=False)
        calls += 1
        if calls == 5:
            print("sleep")
            time.sleep(60)
            calls = 0

def clear_csv(filename):
    f = open(filename, "w+")
    f.close()

historical_data_intraday()
# clear_csv("historical_data_intraday")
print("success")
