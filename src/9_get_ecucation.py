# Get sorted list of agencies that were contacted to report fraud
import os
import csv
import sqlite3

DATA_PATH  = "./data"
OUT_PATH = "../plots"


csv_file = open(os.path.join(OUT_PATH, '9_fraud_education.csv'), "w")
data_writer = csv.writer(csv_file,delimiter=',')


connection = sqlite3.connect('project_data.db')
cursor = connection.cursor()


cursor.execute(
		'''
			SELECT CP.CustomerZip, CP.Crimes, CP.Population, education.CollegePerc FROM
				(SELECT complaints.CustomerZip, COUNT(*) as Crimes, populations.Population FROM complaints
				INNER JOIN populations ON  populations.ZipCode == complaints.CustomerZip
				WHERE complaints.IsCyber = 1
				GROUP BY complaints.CustomerZip) CP
			INNER JOIN education ON education.ZipCode == CP.CustomerZip
	    ''')

cyber_rows = cursor.fetchall()
print(len(cyber_rows))

cursor.execute(
		'''
			SELECT CP.CustomerZip, CP.Crimes, CP.Population, education.CollegePerc FROM
				(SELECT complaints.CustomerZip, COUNT(*) as Crimes, populations.Population FROM complaints
				INNER JOIN populations ON  populations.ZipCode == complaints.CustomerZip
				WHERE complaints.IsCyber = 0
				GROUP BY complaints.CustomerZip) CP
			INNER JOIN education ON education.ZipCode == CP.CustomerZip
	    ''')

reg_rows = cursor.fetchall()


for i in reg_rows:
	for j in cyber_rows:
		if list(i)[0] == list(j)[0]: #same zipcodes
			try:
				new_row = [list(i)[0], list(i)[1], list(i)[2], list(i)[3], float(list(i)[1])*1000/float(list(i)[2]), list(j)[1], list(j)[2], list(j)[3], float(list(j)[1])*1000/float(list(j)[2])]
				data_writer.writerow(new_row)
			except:
				aaaa=1
