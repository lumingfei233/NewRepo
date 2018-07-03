import re
import numpy as np
        
fp = open("./cc_co.rpt")
count = 0
bingo = 0
cc_co = []
flag = (" O  (", " I  (", " B  (")

def inum(string, C):
    num = re.findall(r"\d+", string)
    cc = ( int(num[0])**2 + int(num[1])**2 ) **0.5
    co = int(num[2])
    C.append([cc, co])

while True:
    fl = fp.readline()
    if(fl == ''):
        break
     
    if(flag[0] in fl):
        s = fl.partition(flag[0])
        inum(s[2], cc_co)
        count += 1
    if(flag[1] in fl):
        s = fl.partition(flag[1])
        if(s[2][0] == ')'):
            continue
        inum(s[2], cc_co)
        count += 1
    if(flag[2] in fl):
        s = fl.partition(flag[2])
        inum(s[2], cc_co)
        count += 1       
print(count)

