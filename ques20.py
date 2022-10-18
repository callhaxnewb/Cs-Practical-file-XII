client_detail=[]
def add():
    while True:
        print("Adding a new record in client detail...")
        i=int(input("Enter client's ID: "))
        j=input("Enter client's name: ")
        k=int(input("Enter client's number"))
        det=(i,j,k)
        client_detail.append(det)
        c=input("Do you want to add more records? (y/n)")
        if c=='y':
            continue
        elif c=='n':
            break
def delete():
    while True:
        print("Deleting a record from client detail")
        d=int(input("Enter Id of client to be deleted from record: "))
        k=[]
        for i in client_detail:
            if k[0]==d:                                                                                  ####f
                continue
            else:
                k.append(i)
        for j in k:
            client_detail.append(j)
        c=input("Do you want to delete more records? (y/n)")
        if c=='y':
            continue
        else:
            break

def search():
    print("Searching a record from client detail...")
    i=int(input("Do you want to search client by ID,Name or Contact number? (1,2,3)"))
    
    if i==1:
        j=int(input("Enter client ID: "))
        for i in client_detail:
            if i[0]==j:
                print(i)
    if i==2:
        j=input("Enter client name: ")
        for i in client_detail:
            if i[1]==j:
                print(i)
    if i==3:
        j=int(input("Enter client's number:"))
        for i in client_detail:
            if i[2]==j:
                print(i)

print('''
Select option:
1. Add record
2. Delete record
3. Search record
''')
i=int(input("Choice: "))

if i==1:
    add()
elif i==2:
    delete()
elif i==3:
    search()
    
