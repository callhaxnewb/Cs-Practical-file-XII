f=open('test1.txt','r')
count=0
for line in f:
    for words in line:
        for i in words:
            for j in i:
                count=count+1
print("Size of file in bytes:",count)
