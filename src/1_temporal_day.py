# The main sripts that dumps all the datasets into the tables for querying
import os
import csv
import sqlite3


DATA_PATH  = "./data"
OUT_PATH = "../plots"


csv_file = open(os.path.join(OUT_PATH, '1_temporal_day.csv'), "w")
data_writer = csv.writer(csv_file,delimiter=',')

connection = sqlite3.connect('project_data.db')
cursor = connection.cursor()

cursor.execute(
		'''
			SELECT Count(Day), Day, Month, Year FROM complaints
			WHERE IsCyber = 1
			GROUP BY Year, Month, Day
			ORDER BY Year ASC, Month ASC, Day ASC

	    ''')

cyber_rows = cursor.fetchall()

cursor.execute(
		'''
			SELECT Count(Day), Day, Month, Year FROM complaints
			WHERE IsCyber = 0
			GROUP BY Year, Month, Day
			ORDER BY Year ASC, Month ASC, Day ASC

	    ''')
reg_rows = cursor.fetchall()

for i in reg_rows:
	for j in cyber_rows:

		if str(list(i)[1:4]) == str(list(j)[1:4]):
			new_date = str(list(i)[3])+str(list(i)[2])+str(list(i)[1])
			new_row = [new_date, i[0], j[0]]
			data_writer.writerow(new_row)


