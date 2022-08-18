from records import *
import datetime as dt

class Transaction:
    def __init__(self, send, rec, amt, dt: dt.datetime) -> None:
        self.sender = send
        self.receiver = rec
        self.amount = amt
        self.datetime = dt
        
    def to_String(self):
        out = self.datetime + ": " + self.sender + "," +self.receiver + "," + self.amount
        return 

class Ledger(Record):
    def __init__(self, path = "/cache/ledger.txt", tList = [], *transactions: Transaction) -> None:
        super().__init__(path, tList, *transactions)