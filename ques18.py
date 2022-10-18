flight_detail=[]
def Addflight():
    while True:
        print("Adding a new record in flight detail...")
        i=int(input("Enter flight's number: "))
        j=input("Enter flight's name: ")
        k=int(input("Enter flight's fare"))
        det=(i,j,k)
        flight_detail.append(det)
        c=input("Do you want to add more records? (y/n)")
        if c=='y':
            continue
        elif c=='n':
            break
def Deleteflight():
    while True:
        print("Deleting a record from flight detail")
        d=int(input("Enter number of flight to be deleted from record: "))
        k=[]
        for i in flight_detail:
            if k[0]==d:                                                                                  ####f
                continue
            else:
                k.append(i)
        for j in k:
            flight_detail.append(j)
        c=input("Do you want to delete more records? (y/n)")
        if c=='y':
            continue
        else:
            break
def Displayflight():
    for i in flight_detail:
        print(i)


print('''
Select option:
1. Add record
2. Delete record
3. Display record
''')
i=int(input("Choice: "))
j=0
while j==0:
    if i==1:
        Addflight()
    elif i==2:
        Deleteflight()
    elif i==3:
        Displayflight()

    
