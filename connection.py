import ibapi

from ibapi.client import EClient
from ibapi.wrapper import EWrapper

from ibapi.contract import Contract
from ibapi.order import *
import threading
import time

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def realtimeBar(self, reqId, time: int, open_: float, high: float, low: float, close: float, volume: int, wap: float, count: int):
        super().realtimeBar(reqId, time, open_, high, low, close, volume, wap, count)
        try:
            bot.on_bar_update(reqId, time, open_, high, low, close, volume, wap, count)
        except Exception as e:
            print(e)
    
    def error(self, id, errorCode, errorMsg):
        print("FUCK")
        print(errorCode)
        print(errorMsg)

class Bot:
    ib = None
    def __init__(self):
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 7496,1)
        ib_thread = threading.Thread(target=self.run_loop, daemon=True)
        ib_thread.start()
        time.sleep(1)
        symbol = input("Enter the symbol you want to trade: ")
        contract = Contract()
        contract.symbol = symbol.upper()
        contract.secType = "NEWS"
        contract.exchange = "BRFG"
        contract.currency = "USD"
        self.ib.reqRealTimeBars(0,contract,5,"TRADES",1,[])
    
    def run_loop(self):
        self.ib.run()

    def on_bar_update(self, reqId, time: int, open_: float, high: float, low: float, close: float, volume: int, wap: float, count: int):
        print(reqId)

bot = Bot()
