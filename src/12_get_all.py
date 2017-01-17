


# Get sorted list of agencies that were contacted to report fraud
import os
import csv
import sqlite3

DATA_PATH  = "./data"
OUT_PATH = "../plots"



csv_file = open(os.path.join(OUT_PATH, '12_all_cyber.csv'), "w")
data_writer = csv.writer(csv_file,delimiter=',')


connection = sqlite3.connect('project_data.db')
cursor = connection.cursor()

cursor.execute(
		'''
			SELECT complaints.CustomerZip, COUNT(*) as A, populations.Population, ages.Age, incomes.MedianIncome, education.CollegePerc, employment.Unemployed, races.PercWhite, races.PercBlack, races.PercAsian, races.PercLatin 
			FROM complaints 
				JOIN populations 
					ON populations.ZipCode = complaints.CustomerZip
				JOIN races 
					ON races.ZipCode = complaints.CustomerZip
				JOIN ages 
					ON ages.ZipCode = complaints.CustomerZip
				JOIN incomes 
					ON ages.ZipCode = complaints.CustomerZip
				JOIN education 
					ON education.ZipCode = complaints.CustomerZip
				JOIN employment 
					ON education.ZipCode = complaints.CustomerZip	
			WHERE complaints.IsCyber = 1
			GROUP BY complaints.CustomerZip
	    ''')

cyber_rows = cursor.fetchall()

for i in cyber_rows:
	data_writer.writerow(list(i))

