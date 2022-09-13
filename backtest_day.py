import csv
from subprocess import HIGH_PRIORITY_CLASS
import requests
import pandas as pd
import time
from os.path import exists

def main():
    global stock, filename, trend_stats
    stock = input("Enter a stock ticker symbol: ")
    filename = "1day_{}.csv".format(stock)
    trend_stats = [(12,3),(10,1),(11,2)]

def historical_data_daily():
    if exists(filename):
        keep_going = input("This backtest has already been run, would you like to run it again? [Y/N]: ")
        if keep_going == "N":
            return
    global df
    clear_csv(filename)
    # url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={}&datatype=csv&apikey=IWSS4R694TVBE5LG".format(stock)
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&datatype=csv&apikey=IWSS4R694TVBE5LG".format(stock)
    df = pd.read_csv(url)
    if len(df) < 50:
        print("NOT WORTH IT LMAO")
        return
    supertrends()
    df.to_csv(filename, mode="a", index=False)

def supertrends():        # starting place for calculating atr and supertrends
    calc_tr()       # calculates true ranges and subsequently ATRs
    for set in trend_stats:
        mult = set[1]
        length = set[0]
        atr_name = "ATR-{}".format(length)
        trend_name = "Supertrend-{}".format(mult)
        for i in range(len(df) - length - 1, 0, -1):
            basic = calc_basic(mult, i, atr_name)
            final = calc_final(basic, i)
            spr = calc_super(final, i)
            df.at[i,trend_name] = spr

def calc_basic(mult, index, atr_name):
    high = df.at[index, "high"]
    low = df.at[index, "low"]
    atr = df.at[index, atr_name]
    upper = ((high + low) / 2) + (mult * atr)
    lower = ((high + low) / 2) - (mult * atr)
    return [upper, lower]

def calc_final(basic, index):
    


    
def calc_tr():          # calculate true range for each day and call for average true range
    df["TR"] = 0
    for i in range(0,len(df) - 1):      # each day except first as you need previous close
        prev = df.iloc[i + 1]
        cur = df.iloc[i]
        high = cur.loc["high"]
        low = cur.loc["low"]
        prev_close = prev.loc["close"]
        tr = max((high - low), abs(high - prev_close), abs(low - prev_close))
        df.iloc[i] = df.iloc[i].replace(0,tr)
    calc_atr()

def calc_atr():        # use true ranges for ATRs
    for set in trend_stats:
        length = set[0]     # number of datapoints in ATR
        atr_name = "ATR-{}".format(length)
        trend_name = "Supertrend-{}".format(set[1])
        df[atr_name] = 0        # create new columns with apt names
        df[trend_name] = 0
        df.at[len(df) - length,atr_name] = first_atr(length)
        for i in range(len(df) - length - 1, -1, -1):    # loop from day to the length of ATR days back
            prev_atr = df.at[i, atr_name]
            cur_tr = df.at[i,"TR"]
            df.at[i,atr_name] = ((prev_atr * length) + cur_tr) / length + 1

def first_atr(length):      # calculate first ATR with brute force
    atr = 0
    for i in range(len(df) - length, len(df)):
        row = df.iloc[i]
        atr += row.loc["TR"]
    return atr / length

def clear_csv(filename):
    f = open(filename, "w+")
    f.close()

if __name__ == "__main__":
    main()
    historical_data_daily()
    print("success")
