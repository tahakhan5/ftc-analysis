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
			SELECT Count(*) as A, geodata.MSAName FROM geodata
			INNER JOIN complaints ON  geodata.ZipCode == complaints.FraudZip
			WHERE complaints.IsCyber = 1
			GROUP BY geodata.MSAName
			Order BY A DESC
	    ''')


cyber_rows = cursor.fetchall()

cursor.execute(
		'''
			SELECT Count(*) as A, geodata.MSAName FROM geodata
			INNER JOIN complaints ON  geodata.ZipCode == complaints.FraudZip
			WHERE complaints.IsCyber = 0
			GROUP BY geodata.MSAName
			Order BY A DESC
	    ''')

reg_rows = cursor.fetchall()

for i in reg_rows:
	for j in cyber_rows:

		if list(i)[1] == list(j)[1]:
			new_row = [list(i)[1], list(i)[0], list(j)[0]]
			data_writer.writerow(new_row)

