import sys
import operator

# file = open("D:\python project\hackathon2018\q3\sample-p2.1.in","r", encoding="utf8")

file = sys.stdin

head = file.readline()

data ={}
user={}

def toDit(dict,key,val):
    if key in data:
        dict[key] += val
    else:
        dict[key] = val

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

    # count time to use
    toDit(data,CMPGN_TYPE_DESC,1)

    if CMPGN_TYPE_DESC in user:
        if CUSTOMER_ID not in user[CMPGN_TYPE_DESC]:
            user[CMPGN_TYPE_DESC].append(CUSTOMER_ID)
    else:
        user[CMPGN_TYPE_DESC] = [CUSTOMER_ID]

result = []

for i in data:
    str1 = i +' '+ str(round(data[i]/len(user[i]),2))
    # print(data[i],len(user[i]))
    result.append(str1)

print(*sorted(result) ,sep="\n")