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

bot = Bot()
