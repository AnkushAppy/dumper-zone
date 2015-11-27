
import csv

filename1 = 'AllstarFull.csv' 
f1= open(filename1, 'rb') # open file with read only permission
reader = csv.reader(f1)   # read file (csv particularly)

filename2='trialoutput.csv'
f2= open(filename2, 'wb')
writer = csv.writer(f2,delimiter='\t', quotechar='"')

for row in reader:        # for every row of reader
     writer.writerow([row[0],delimiter , row[3]])  # write row 0, 3 


f1.close()
f2.close()


