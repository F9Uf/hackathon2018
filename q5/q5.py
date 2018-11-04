import sys
import time

def toStructTime (str):
    hour = int(str.split(':')[0])
    minut = int(str.split(':')[1])
    s = int(str.split(':')[2])

    # print(hour,minut,s)
    return time.mktime(time.struct_time((2010, 10, 1, hour, minut, s, 0, 0, 0)))

file = open("D:\python project\hackathon2018\q5\sample-p5.1.in","r", encoding="utf8")

# file = sys.stdin

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
        "DAY" : REDEMP_DT,
        "TIME": REDEMP_TM,
        "TIMESTAMP" : toStructTime(REDEMP_TM)
    }

    data.append(line)

new_data = sorted(data ,key=lambda k: k['TIME'])
new_data = sorted(new_data, key=lambda k: k['DAY'])

result = []

for i in range(len(new_data)):
    start = new_data[i]
    j = 0
    while new_data[j+i]['DAY'] == new_data[i]['DAY'] and (j+i)<len(new_data)-1:
        j = j+1
    count = j
    end = new_data[count]
    result.append({
        "start": start['TIME'],
        "end": end['TIME'],
        "how": float(end['TIMESTAMP'])-float(start['TIMESTAMP']),
        "count": count
    })
    i = i + count

result = list(filter(lambda x: x['how']<20*60*1000, result ))
max_val = max(result, key=lambda x: x['count'])
print(*sorted(result, key=lambda x: x['count']), sep='\n')

