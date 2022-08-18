import hashlib
import os
import datetime as dt
from blockchain import *
from ledger import *

class User:
    def __init__(self, name, date: dt.datetime, id = None, dateRec = None) -> None:
        self.name = name
        self.dateRegistered = date
        if id:
            self.hashID = id
        else:
            self.hashID = hashlib.sha256(self.data.encode()).hexdigest()
        if dateRec:
            self.dateRecorded = dateRec
        else:
            self.dateRecorded = dt.datetime.now()
        self.data = str(self.dateRecorded)+","+self.name+","+str(self.dateRegistered)
        
    def to_String(self):
        return self.hashID + "," + self.data
    
    def print_Data(self):
        print(self.data)
        
 
class Wallet:
    def __init__(self, owner: User, password, date: dt.datetime, id = None, usdBal = 0, bdcBal = 0) -> None:
        self.ownerHashID = owner.hashID
        self.password = password
        self.dateRegistered = date
        self.balanceBDC = bdcBal
        self.balanceUSD = usdBal
        self.immutData = str(self.dateRegistered) + "," + self.ownerHashID + "," + str(self.password)
        self.data = self.immutData + "," + str(self.balanceBDC) + "," + str(self.balanceUSD)
        self.hashID = hashlib.sha256(self.immutData.encode()).hexdigest()
        
    def to_String(self):
        return self.hashID + "," + self.data