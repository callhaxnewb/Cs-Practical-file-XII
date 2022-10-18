import csv
def rankers():
    f=open("student.csv",'r')
    h=csv.reader(f)
    pm=80
    a=''
    while a:
              
        for row in h:
            detail=row.split(',')
            if detail[2]>=hm:
                print(detail)
            else:
                continue


rankers()
