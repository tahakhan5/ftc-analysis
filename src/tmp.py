# Get sorted list of agencies that were contacted to report fraud
import os
import csv
import sqlite3

DATA_PATH  = "./data"
OUT_PATH = "../plots"


csv_file = open(os.path.join(OUT_PATH, '7_tmp.csv'), "w")
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

for x in cyber_rows:
	print(x)



Zipcode, Crime Count, Population, Median Age


cursor.execute(
		'''
			SELECT  age.ZipCode, SUM(Tab.Population), geodata.MSAName FROM 
				

				(SELECT complaints.FraudZip, COUNT(*), populations.Population FROM complaints
				INNER JOIN populations ON  populations.ZipCode == complaints.FraudZip
				WHERE complaints.IsCyber = 1) complaint_pop



			INNER JOIN geodata ON geodata.ZipCode == Tab.FraudZip
			GROUP BY geodata.MSAName
			Order BY A DESC
	    ''')