import csv, codecs
import random


fileName = "./sqlite/student_try.csv"
fp = codecs.open(fileName,"r",encoding="utf-8")

reader = csv.reader(fp, delimiter=',', quotechar='"')

with codecs.open('./crawl/output.csv', 'w', encoding='utf-8') as ff:
    writer = csv.writer(ff, delimiter=',', quotechar='"')

    for cells in reader:
        writer.writerow([cells[0], random.randrange(1,100)])