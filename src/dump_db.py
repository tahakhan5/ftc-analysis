# The main sripts that dumps all the datasets into the tables for querying
import os
import csv
import sqlite3
from collections import Counter


	
DATA_PATH  = "./data"


CONTACT_METHODS = {'regular': set(['Phone Call: Mobile/Cell', 'Wireless', 'Phone Call: Landline', 'Phone']), \
           'cyber': set(['Internet (Other)', 'Social Network', 'Mobile: Text/Email/IM', 'Internet Web Site', 'Email', 'Internet/E-mail'])}


TRUE_CYBERCRIMES = set(['Spyware\Adware\Malware', 'Internet Information Services', 'Internet Access Services', 'Internet Auction', \
						 'Internet Web Site Design\Promotion', 'Social Networking Service'])


connection = sqlite3.connect('project_data.db')
cursor = connection.cursor()


def callibrate_zip(zipcode):
# Eliminate all zipcodes that are inconsistent with the US 5 digit zip preference
	new_zip = '99999'
	if zipcode == "NULL" or zipcode.isdigit() == False or len(zipcode) >5 or zipcode == "":
		return new_zip
	else:	
		if len(zipcode) == 5:
			new_zip = zipcode
		else:
			new_zip = '0'*(5-len(zipcode))+zipcode
		return new_zip


def is_cyber( contactmethod, fraudtype):
	if contactmethod in CONTACT_METHODS['cyber']:
		return 1
	else:
		if fraudtype in TRUE_CYBERCRIMES:
			return 1
	return 0


def add_ftc_data():
		count = 0
		cursor.execute(
		'''
			CREATE TABLE complaints(
				Organization TEXT, 
	        	CustomerZip TEXT, 
	        	FraudZip TEXT, 
	        	ContactMethod TEXT,
	        	SecContactMethod TEXT,
	        	FraudType TEXT,
	        	FraudDate DATE,
	        	ReportingDate DATE,
	        	IsCyber BOOLEAN,
	        	Day INT,
	        	Month INT,
	        	Year INT)
	    ''')

		connection.commit()

		with open(os.path.join(DATA_PATH, 'ftc_data.csv')) as csvfile:
		  	reader = csv.DictReader(csvfile)
		  	for line in reader:
		  		try:

			  		Organization = line['OrganizationName']
			  		CustomerZip = callibrate_zip(line['Consumer-ZipCode'])
			  		FraudZip = callibrate_zip(line['Company-ZipCode'])
			  		ContactMethod = line['InitialContactMethodDesc']
			  		SecContactMethod = line['AgencyContactMethodDesc']
			  		FraudType = line['ProductCodeDesc']
			  		FraudDate = line['InitialContactDate']
			  		ReportingDate = line['AgencyContactDate']
			  		IsCyber = is_cyber(ContactMethod, FraudType)
			  		Day = ReportingDate.split("/")[1]
			  		Month = ReportingDate.split("/")[0]
			  		Year = ReportingDate.split("/")[2]

			  		data = (Organization, CustomerZip, FraudZip, ContactMethod, SecContactMethod, FraudType, FraudDate, ReportingDate, IsCyber, Day, Month, Year)
			  		cursor.execute("INSERT INTO complaints VALUES %s " % str(data))
			  		count = count+1;
			  	except Exception as e:
			  		print(e)
			  		continue


def add_income_data():
	cursor.execute(
	'''
		CREATE TABLE incomes(
			ZipCode TEXT PRIMARY KEY,
			Employment INT, 
        	MedianIncome INT)
    ''')

	connection.commit()

	with open(os.path.join(DATA_PATH, 'income_data.csv')) as csvfile:
	  	reader = csv.DictReader(csvfile)
	  	for line in reader:

	  		ZipCode = line['GEO.display-label'].split(" ")[1]
	  		Employment  = line['HC01_VC03']
	  		MedianIncome = line['HC01_VC85']

	  		if len(Employment) > 0 and len(MedianIncome):
		  		data = (ZipCode, Employment, MedianIncome)
		  		cursor.execute("INSERT INTO incomes VALUES %s " % str(data))


def add_population_data():
	cursor.execute(
	'''
		CREATE TABLE populations(
			ZipCode TEXT PRIMARY KEY,
			Population INT)
    ''')

	connection.commit()

	with open(os.path.join(DATA_PATH, 'population_data.csv')) as csvfile:
	  	reader = csv.DictReader(csvfile)
	  	for line in reader:

	  		ZipCode = line['GEO.display-label'].split(" ")[1]
	  		Population  = line['HD01_VD01']

	  		if len(Population) > 0:
		  		data = (ZipCode, Population)
		  		cursor.execute("INSERT INTO populations VALUES %s " % str(data))



def add_age_data():
	cursor.execute(
	'''
		CREATE TABLE ages(
			ZipCode TEXT PRIMARY KEY,
			Age INT)
    ''')

	connection.commit()

	with open(os.path.join(DATA_PATH, 'age_data.csv')) as csvfile:
	  	reader = csv.DictReader(csvfile)
	  	for line in reader:

	  		ZipCode = line['GEO.display-label'].split(" ")[1]
	  		Age = line['HC01_EST_VC35']

	  		if len(Age) > 0:
		  		data = (ZipCode, Age)
		  		cursor.execute("INSERT INTO ages VALUES %s " % str(data))



def add_college_data():
	cursor.execute(
	'''
		CREATE TABLE education(
			ZipCode TEXT PRIMARY KEY,
			CollegePerc REAL)
    ''')
	
	with open(os.path.join(DATA_PATH, 'college_data.csv')) as csvfile:
		reader = csv.DictReader(csvfile)
		for line in reader:
			try:
				ZipCode = line['ZIPCODE']
				PercCollege = line['PERC'].split(" ")[0]

				if len(ZipCode) > 0 and len(PercCollege):

					data = (ZipCode, PercCollege)
					cursor.execute("INSERT INTO education VALUES %s " % str(data))
			except:
				continue



def add_race_data():
	cursor.execute(
	'''
		CREATE TABLE races(
			ZipCode TEXT PRIMARY KEY,
			PercWhite REAL,
			PercBlack REAL,
			PercAsian REAL,
			PercNative REAL,
			PercLatin REAL)
    ''')

	connection.commit()
	count = 0

	with open(os.path.join(DATA_PATH, 'race_data.csv')) as csvfile:
		reader = csv.DictReader(csvfile)
		for line in reader:

			ZipCode = line['GEO.display-label'].split(" ")[1]
			PercWhite = line['HC03_VC49']
			PercBlack = line['HC03_VC50']
			PercAsian = line['HC03_VC56']
			PercNative = line['HC03_VC51']
			PercLatin = line['HC03_VC88']

			if len(PercWhite) > 0 and len(PercBlack) > 0 and len(PercAsian) > 0 and len(PercLatin) > 0:
				data = (ZipCode, PercWhite, PercBlack, PercAsian, PercNative, PercLatin)
				cursor.execute("INSERT INTO races VALUES %s " % str(data))


def add_geo_data():
	cursor.execute(
	'''
		CREATE TABLE geodata(
			ZipCode TEXT PRIMARY KEY,
			MsaID TEXT,
			MsaName TEXT,
			State TEXT)
    ''')

	connection.commit()

	with open(os.path.join(DATA_PATH, 'zip_msa_data.csv')) as csvfile:
	  	reader = csv.DictReader(csvfile)
	  	for line in reader:

	  		ZipCode = line['ZIP CODE']
	  		MsaID = line['MSA No.']
	  		MsaName = line['MSA Name']
	  		State = line['STATE']
	  		
	  		if len(MsaID) > 0 and len(MsaName) > 0 and len(State) > 0:
		  		data = (ZipCode, MsaID, MsaName, State)
		  		cursor.execute("INSERT INTO geodata VALUES %s " % str(data))


def main():
	add_college_data()
	add_race_data()
	add_geo_data()
	add_ftc_data()
	add_age_data()
	add_population_data()
	add_income_data()

	connection.commit()

if __name__ == '__main__':
	main()