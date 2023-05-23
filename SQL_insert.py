import sqlite3

data = []
with open ("company.txt",'r') as f:
    for line in f:
        item = line.strip().split(',')
        data.append(tuple([int(item[0]), item[1]]))
print(data)

conn = sqlite3.connect('laptops.db')
cursor = conn.cursor()

cursor.executemany("INSERT INTO Company VALUES(?,?)", data)
conn.commit()

data = []
with open ("DGMT.txt",'r') as f:
    for line in f:
        item = line.strip().split(',')
        data.append(tuple([int(item[0]), item[1]]))
print(data)


cursor.executemany("INSERT INTO RAM VALUES(?,?)", data)
conn.commit()

data = []
with open ("operating_system.txt",'r') as f:
    for line in f:
        item = line.strip().split(',')
        data.append(tuple([int(item[0]), item[1]]))
print(data)

cursor.executemany("INSERT INTO OS VALUES(?,?)", data)
conn.commit()

data = []
with open ("series.txt",'r') as f:
    for line in f:
        item = line.strip().split(',')
        data.append(tuple([int(item[0]), item[1], int(item[2])]))
        print(item)
print(data)
print(1)
cursor.executemany("INSERT INTO Series VALUES(?,?,?)", data)
conn.commit()

data = []
with open ("model.txt",'r') as f:
    for line in f:
        item = line.strip().split(',')
        data.append(tuple([int(item[0]), item[1], int(item[2]), int(item[3]),int(item[4])]))
print(data)

cursor.executemany("INSERT INTO Model VALUES(?,?,?,?,?)", data)
conn.commit()
conn.close()