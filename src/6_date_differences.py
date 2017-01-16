# Get Differences in Dates
import os
import csv
import sqlite3
from datetime import datetime



def days_between(d1, d2):
# function obtained from
#http://stackoverflow.com/questions/8419564/difference-between-two-dates
    d1 = datetime.strptime(d1, "%m/%d/%y")
    d2 = datetime.strptime(d2, "%m/%d/%y")
    return abs((d2 - d1).days)

DATA_PATH  = "./data"
OUT_PATH = "../plots"

connection = sqlite3.connect('project_data.db')

cursor = connection.cursor()

# Get Cyber Dates 
csv_file = open(os.path.join(OUT_PATH, '6_dates_cyber.csv'), "w")


cursor.execute(
		'''
			SELECT FraudDate, ReportingDate FROM complaints
			WHERE IsCyber = 1 AND FraudDate != 'NULL'
	    ''')

cyber_rows = cursor.fetchall()

for x in cyber_rows:
	try:
		if int(days_between(list(x)[0], list(x)[1])) < 366:
			csv_file.write(str(days_between(list(x)[0], list(x)[1]))+"\n")  
	except:
		continue


# Get Regular Dates 
csv_file = open(os.path.join(OUT_PATH, '6_dates_regular.csv'), "w")

cursor.execute(
		'''
			SELECT FraudDate, ReportingDate FROM complaints
			WHERE IsCyber = 0 AND FraudDate != 'NULL'
	    ''')

cyber_rows = cursor.fetchall()

for x in cyber_rows:
	try:

		if int(days_between(list(x)[0], list(x)[1])) < 366:
			csv_file.write(str(days_between(list(x)[0], list(x)[1]))+"\n")  
	except:
		continue


# for x in cyber_rows:
# 	f_zip = zipcode.isequal(list(x)[0])
# 	c_zip = zipcode.isequal(list(x)[1])

# 	if f_zip!= None and c_zip!= None:
# 		f_cord = (f_zip.lat, f_zip.lon)
# 		c_cord = (c_zip.lat, c_zip.lon)
# 		csv_file.write(str(vincenty(f_cord, c_cord).miles)+"\n")


# # Get Regular Distances 
# csv_file = open(os.path.join(OUT_PATH, '5_distances_regular.csv'), "w")
# data_writer = csv.writer(csv_file,delimiter=',')


# cursor.execute(
# 		'''
# 			SELECT FraudZip, CustomerZip FROM complaints
# 			WHERE IsCyber = 0 AND FraudZip != '99999'
# 	    ''')

# cyber_rows = cursor.fetchall()

# for x in cyber_rows:
# 	f_zip = zipcode.isequal(list(x)[0])
# 	c_zip = zipcode.isequal(list(x)[1])

# 	if f_zip!= None and c_zip!= None:
# 		f_cord = (f_zip.lat, f_zip.lon)
# 		c_cord = (c_zip.lat, c_zip.lon)
# 		csv_file.write(str(vincenty(f_cord, c_cord).miles)+"\n")


