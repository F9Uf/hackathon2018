import sys
import operator

file = open("D:\python project\hackathon2018\q2\sample-p2.1.in","r", encoding="utf8")

# file = sys.stdin

head = file.readline()

data ={}

for line in file:
    da = line.split('|')
    CUSTOMER_ID = da[0]
    REDEMP_DT = da[1]
    REDEMP_TM = da[2]
    CAT_DESC = da[3]
    SUB_CAT_DESC = da[4]
    PRNTR_DESC = da[5]
    REDEEM_TYPE_DESC = da[6]
    CMPGN_TYPE_DESC = da[7]
    CHNL = da[8].split('\n')[0]

    pair = CHNL+' '+SUB_CAT_DESC

    if pair in data:
        data[pair] += 1
    else:
        data[pair] = 1
    

max = max(data.items(), key=operator.itemgetter(1))[1]
print(*sorted([k for k, v in data.items() if v == max]))
