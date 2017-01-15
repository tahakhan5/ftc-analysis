# The main sripts that dumps all the datasets into the tables for querying
import os
import csv
import sqlite3


DATA_PATH  = "./data"
OUT_PATH = "../plots"


csv_file = open(os.path.join(OUT_PATH, '2_temporal_month.csv'), "w")
data_writer = csv.writer(csv_file,delimiter=',')

connection = sqlite3.connect('project_data.db')
cursor = connection.cursor()

cursor.execute(
		'''
			SELECT Count(*), Month, Year FROM complaints
			WHERE IsCyber = 1
			GROUP BY Year, Month
			ORDER BY Year ASC, Month ASC
	    ''')

cyber_rows = cursor.fetchall()


cursor.execute(
		'''
			SELECT Count(*), Month, Year FROM complaints
			WHERE IsCyber = 0
			GROUP BY Year, Month
			ORDER BY Year ASC, Month ASC
	    ''')

reg_rows = cursor.fetchall()

for i in reg_rows:
 	for j in cyber_rows:

 		if str(list(i)[1:3]) == str(list(j)[1:3]):

 			new_date = str(str(list(i)[2])+str(list(i)[1]))
 			new_row = [new_date, i[0], j[0]]
 			data_writer.writerow(new_row)


