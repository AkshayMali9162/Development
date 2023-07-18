import csv


opencsvfile = open("C:\\Study Material\\Python Study\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\example.csv",encoding="utf-8")
csvfile  = csv.reader(opencsvfile)


data = list(csvfile)



writecsv = open("C:\\Study Material\\Python Study\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\test.csv",mode = 'w',newline='')
csvfile1 = csv.writer(writecsv,delimiter=",")
csvfile1.writerow(["name","email"])


for da in data[1:3]:
    name = da[1].strip() + ' ' + da[2].strip()
    email = da[3]
    csvfile1.writerow([name,email])

writecsv.close()
    



