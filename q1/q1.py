import sys
import operator

# file = open("D:\python project\hackathon2018\q1\sample-p0.1.in","r", encoding="utf8")

file = sys.stdin

head = file.readline()

data ={}

for line in file:
    da = line.split('|')
    name = da[5]    
    if name in data:
        data[da[5]] += 1
    else:
        data[da[5]] = 1

sort_x = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    
for i in range(5):
	print(sort_x[i][0]+' '+str(sort_x[i][1]))
