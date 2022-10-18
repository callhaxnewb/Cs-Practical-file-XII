import csv
f=open("marks.csv","w+")
'''
g=csv.writer(f)
sum=0
hm=0
data=[['Roll no.','Name','Marks']]
c='y'
while c=='y':
    r=int(input("enter roll no. "))
    n=input("enter name")
    m=int(input("enter marks: "))
    d=[r,n,m]
    data.append(d)
    c=input("enter more?(y/n)")
    sum=sum+m
    if m>hm:
        hm=m
    else:
        continue
g.writerows(data)
print('sum of all marks: ',sum)
print("highest marks: ",hm)

'''
def high():
    f=open("marks.csv")
    h=csv.reader(f)
    hm=0
    ranker=[]
    for row in f:
        detail=row.split(',')
        if detail[2]>hm:
            hm=detail[2]
            ranker=detail
        else:
            continue


high()








            
