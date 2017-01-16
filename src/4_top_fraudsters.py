# Get sorted list of agencies that were contacted to report fraud
import os
import csv
import sqlite3

DATA_PATH  = "./data"
OUT_PATH = "../plots"


csv_file = open(os.path.join(OUT_PATH, '4_top_fraudsters.csv'), "w")
data_writer = csv.writer(csv_file,delimiter=',')

connection = sqlite3.connect('project_data.db')
cursor = connection.cursor()


cursor.execute(
		'''
			SELECT COUNT(*) as A, SUM(Tab.Population), geodata.MSAName FROM 
				(SELECT complaints.FraudZip, populations.Population FROM complaints
				INNER JOIN populations ON  populations.ZipCode == complaints.FraudZip
				WHERE complaints.IsCyber = 1) Tab
			INNER JOIN geodata ON geodata.ZipCode == Tab.FraudZip
			GROUP BY geodata.MSAName
			Order BY A DESC
	    ''')

cyber_rows = cursor.fetchall()



cursor.execute(
		'''
			SELECT COUNT(*) as A, SUM(Tab.Population), geodata.MSAName FROM 
				(SELECT complaints.FraudZip, populations.Population FROM complaints
				INNER JOIN populations ON  populations.ZipCode == complaints.FraudZip
				WHERE complaints.IsCyber = 0) Tab
			INNER JOIN geodata ON geodata.ZipCode == Tab.FraudZip
			GROUP BY geodata.MSAName
			Order BY A DESC
	    ''')

reg_rows = cursor.fetchall()

for i in reg_rows:
	for j in cyber_rows:
		if list(i)[2] == list(j)[2]:
			new_row = [list(i)[2], list(i)[0], list(i)[1], list(j)[0], list(i)[1],  float(list(i)[0])*1000/float(list(i)[1]), float(list(j)[0])*1000/float(list(j)[1])]
			data_writer.writerow(new_row)

