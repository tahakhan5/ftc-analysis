# Top agencies that were contacted
import os
import csv
import sqlite3


DATA_PATH  = "./data"
OUT_PATH = "../plots"


csv_file = open(os.path.join(OUT_PATH, 'top_agencies.csv'), "w")
data_writer = csv.writer(csv_file,delimiter=',')

connection = sqlite3.connect('project_data.db')
cursor = connection.cursor()

cursor.execute(
		'''
			SELECT Count(*) as A, Organization FROM complaints
			WHERE IsCyber = 1
			GROUP BY Organization
			ORDER BY A Desc

	    ''')

cyber_rows = cursor.fetchall()

cursor.execute(
		'''
			SELECT Count(*) as A, Organization FROM complaints
			WHERE IsCyber = 0
			GROUP BY Organization
			ORDER BY A Desc
	    ''')

reg_rows = cursor.fetchall()

for i in reg_rows:
	for j in cyber_rows:

		if list(i)[1] == list(j)[1]:
			new_row = [list(i)[1], list(i)[0], list(j)[0]]
			data_writer.writerow(new_row)

