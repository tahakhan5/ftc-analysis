# Get Zipdode distacnes
import os
import csv
import sqlite3
import zipcode
import geopy
from geopy.distance import vincenty


DATA_PATH  = "./data"
OUT_PATH = "../plots"

connection = sqlite3.connect('project_data.db')

cursor = connection.cursor()

# Get Cyber Distances 
csv_file = open(os.path.join(OUT_PATH, '5_distances_cyber.csv'), "w")



cursor.execute(
		'''
			SELECT FraudZip, CustomerZip FROM complaints
			WHERE IsCyber = 1 AND FraudZip != '99999'
	    ''')

cyber_rows = cursor.fetchall()

for x in cyber_rows:
	f_zip = zipcode.isequal(list(x)[0])
	c_zip = zipcode.isequal(list(x)[1])

	if f_zip!= None and c_zip!= None:
		f_cord = (f_zip.lat, f_zip.lon)
		c_cord = (c_zip.lat, c_zip.lon)
		csv_file.write(str(vincenty(f_cord, c_cord).miles)+"\n")


# Get Regular Distances 
csv_file = open(os.path.join(OUT_PATH, '5_distances_regular.csv'), "w")
data_writer = csv.writer(csv_file,delimiter=',')


cursor.execute(
		'''
			SELECT FraudZip, CustomerZip FROM complaints
			WHERE IsCyber = 0 AND FraudZip != '99999'
	    ''')

cyber_rows = cursor.fetchall()

for x in cyber_rows:
	f_zip = zipcode.isequal(list(x)[0])
	c_zip = zipcode.isequal(list(x)[1])

	if f_zip!= None and c_zip!= None:
		f_cord = (f_zip.lat, f_zip.lon)
		c_cord = (c_zip.lat, c_zip.lon)
		csv_file.write(str(vincenty(f_cord, c_cord).miles)+"\n")


