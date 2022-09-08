import ibapi

from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

class Bot:
    ib = None
    def __init__(self):
        ib = IBApi()
        ib.connect("127.0.0.1", 7496,1)
        ib.run()

bot = Bot()
