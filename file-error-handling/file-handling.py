import csv
import json

# berkas txt
namefile = 'berkas/file_01.txt'
file = open(namefile)
data = file.read()
print(data)
# data2 = file.readlines()
# print(data2)

# berkas csv
namafilecsv = 'berkas/file_02.csv'
file = open(namafilecsv)
data = csv.reader(file, delimiter=",")
for item in data:
    print(item)

# berkas json
file = open('berkas/file_03.json')
data = json.load(file)
print(data)
