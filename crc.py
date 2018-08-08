from itertools import product
import crcmod.predefined
from math import factorial
import string
 

found = False
currLen = 1
crcTarget = 0
 

def crc(data):
        crcInstance = crcmod.predefined.Crc("crc-16")
        crcInstance.update(str(data).encode("utf-8", "replace"))
        return crcInstance.crcValue
 
def nCr(n,r):
    f = factorial
    return round(f(n) / f(r) / f(n-r))
 
crcTargetListPre = ["fb38","8cc2","55a5","4f1a","318a"]
crcTargetList = [ hex(int(n, 16)) for n in crcTargetListPre]
for x in crcTargetList:
  print (x)

availableChars = string.digits

while True:
        for possibleCombination in product(availableChars, repeat=currLen):
                currTxt = "".join(possibleCombination)
                currTxt = "Agent 3oH ID " + currTxt
                currCrc = hex(crc(currTxt))

                if currCrc in crcTargetList:
                        found = True
                        print ("COLLISION FOUND: " + currTxt + ": " + currCrc)
 
        currLen = currLen + 1
 
        if found:
                if input("\nContinue searching? Y/N ").upper() == "Y":
                        found = False
                else:
                        break
        else:
                print ("Nothing found.")