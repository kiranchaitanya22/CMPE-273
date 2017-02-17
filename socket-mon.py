import psutil
import collections
import operator
import csv
import sys
dict = {}
x=0
i=0
j = 0
m = 0
dict={}
c={}
for i in sorted(psutil.net_connections(kind='inet'), key=lambda p: p.pid):
    if i.raddr and i.laddr:
        dict[j]=[i.pid,i.laddr[0],i.raddr[0],i.status]
        j=j+1
a = []
for i in dict:
    if dict[i][0] not in a:
        a.append(dict[i][0])
        c[a.index(dict[i][0])]=1
    else:
        c[a.index(dict[i][0])]=c[a.index(dict[i][0])]+1
i = 0
while i < len(a):
    a[i]=[a[i],c[i]]
    i = i + 1
a=sorted(a,key=operator.itemgetter(1),reverse=True)

for k in range(0,len(a)):
    for l in range(0,len(dict)):
        if a[k][0]==dict[l][0]:
            dict[m]=dict[l]
            m=m+1
writer=csv.writer(sys.stdout)
writer.writerow(["Pid","Laddr","Raddr","Status"])
for key, value in dict.iteritems():
    writer.writerow(value)

