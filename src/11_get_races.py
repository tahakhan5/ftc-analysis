# Get sorted list of agencies that were contacted to report fraud
import os
import csv
import sqlite3

DATA_PATH  = "./data"
OUT_PATH = "../plots"



csv_file = open(os.path.join(OUT_PATH, '11_fraud_races.csv'), "w")
data_writer = csv.writer(csv_file,delimiter=',')


connection = sqlite3.connect('project_data.db')
cursor = connection.cursor()


cursor.execute(
		'''
			SELECT CP.CustomerZip, CP.Crimes, CP.Population, races.PercWhite, races.PercBlack, races.PercAsian, races.PercLatin  FROM
				(SELECT complaints.CustomerZip, COUNT(*) as Crimes, populations.Population FROM complaints
				INNER JOIN populations ON  populations.ZipCode == complaints.CustomerZip
				WHERE complaints.IsCyber = 1
				GROUP BY complaints.CustomerZip) CP
			INNER JOIN races ON races.ZipCode == CP.CustomerZip
	    ''')

cyber_rows = cursor.fetchall()
cursor.execute(
		'''
			SELECT CP.CustomerZip, CP.Crimes, CP.Population, races.PercWhite, races.PercBlack, races.PercAsian, races.PercLatin  FROM
				(SELECT complaints.CustomerZip, COUNT(*) as Crimes, populations.Population FROM complaints
				INNER JOIN populations ON  populations.ZipCode == complaints.CustomerZip
				WHERE complaints.IsCyber = 0
				GROUP BY complaints.CustomerZip) CP
			INNER JOIN races ON races.ZipCode == CP.CustomerZip
	    ''')

reg_rows = cursor.fetchall()
for i in reg_rows:
	for j in cyber_rows:
		if list(i)[0] == list(j)[0]: #same zipcodes
			try:
				new_row = [list(i)[0], list(i)[1], list(i)[2], float(list(i)[1])*1000/float(list(i)[2]), float(list(j)[1])*1000/float(list(j)[2]), list(i)[3], list(i)[4], list(i)[5], list(i)[6]]
				data_writer.writerow(new_row)
			except:
				continue