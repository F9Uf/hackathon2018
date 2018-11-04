import sys

# file = open("D:\python project\hackathon2018\q0\sample-p0.1.in","r", encoding="utf8")

file = sys.stdin

head = file.readline()

for line in file:
    da = line.split('|')
    
    if da[0] == "150428059":
        print(da[6])

