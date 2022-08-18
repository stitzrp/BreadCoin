import datetime as dt
import random as r
import os
from breadcoin import * 

namesPath = "./data/names.txt"
peoplePath = "./data/people.txt"
walletsPath = "./data/wallets.txt"
    
def populate_people():
    with open(namesPath) as rfd:
        people = []
        for x in rfd.readlines():
            name = x.split("\n")[0]
            randomDate = dt.datetime(2022, r.randrange(1,13), r.randrange(1, 29), r.randrange(0,24), r.randrange(0,60), r.randrange(0,60))
            p = User(name, randomDate)
            people.append(p)
        with open(peoplePath, "w") as wfd:
            for x in people:
                wfd.write(x.to_String() + "\n")    

def populate_wallets():
    wallets = []
    if os.path.exists(walletsPath):
        with open(walletsPath) as wfd:
            for n in wfd.readlines():
                wallets.append(n.split("\n")[0])
    else:
        with open(walletsPath, "w") as fd:
            for i in range(50):
                num = r.randrange(100000,999999)
                fd.write(str(num) + "\n")
                wallets.append(num)
                
    owners = []
    with open(peoplePath) as pfd:
        for p in pfd.readlines():
            p = p.split("\n")[0]
            fields = p.split(",")
            u = User(fields[2], fields[3], fields[0], fields[1])
            owners.append(u)
    with open(walletsPath, "w") as wfd:
        for i in range(50):
            randomDate = dt.datetime(2022, r.randrange(1,13), r.randrange(1, 29), r.randrange(0,24), r.randrange(0,60), r.randrange(0,60))
            wfd.write(Wallet(owners[i], wallets[i], randomDate).to_String() + "\n")
    
            
        
populate_wallets()
        