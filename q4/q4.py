import sys

# file = open("D:\python project\hackathon2018\q4\sample-p4.1.in","r", encoding="utf8")

file = sys.stdin

head = file.readline()

data = []

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

    line = {
        "ID" : CUSTOMER_ID,
        "TIME" : REDEMP_DT+' '+REDEMP_TM,
        "CAT": CAT_DESC,
        "PRNTR": PRNTR_DESC
    }

    data.append(line)
    
newlist = sorted(data, key=lambda k: k['TIME'])

newlist = sorted(newlist, key=lambda k: k['ID'])

n = 0
k = 0
for i in range(len(newlist)):
    if newlist[i]['PRNTR'] == 'Cafe Amazon' and newlist[i]['ID'] == newlist[i+1]['ID']:
        n = n+1
        if newlist[i+1]['CAT'] == 'Dining':
            k = k +1


print("{0:.2f}".format(k/n))
