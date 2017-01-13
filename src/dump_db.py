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
	cursor.execute(
	'''
		CREATE TABLE complaints(
			Organization TEXT, 
        	CustomerZip TEXT, 
        	FraudZip TEXT, 
        	ReportingMethod TEXT,
        	SecReportingMethod TEXT,
        	FraudType TEXT,
        	FraudDate DATE,
        	ReportingDate DATE,
        	IsCyber BOOLEAN)
    ''')

	connection.commit()

	with open(os.path.join(DATA_PATH, 'ftc_data.csv')) as csvfile:
	  	reader = csv.DictReader(csvfile)
	  	for line in reader:

	  		Organization = line['OrganizationName']
	  		CustomerZip = callibrate_zip(line['Consumer-ZipCode'])
	  		FraudZip = callibrate_zip(line['Company-ZipCode'])
	  		ReportingMethod = line['InitialContactMethodDesc']
	  		SecReportingMethod = line['AgencyContactMethodDesc']
	  		FraudType = line['ProductCodeDesc']
	  		FraudDate = line['InitialContactDate']
	  		ReportingDate = line['AgencyContactDate']
	  		IsCyber = is_cyber(ReportingMethod, FraudType)

	  		data = (Organization, CustomerZip, FraudZip, ReportingMethod, SecReportingMethod, FraudType, FraudDate, ReportingDate, IsCyber)
	  		cursor.execute("INSERT INTO complaints VALUES %s " % str(data))




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

	  		data = (ZipCode, Age)
	  		print(data)
	  		cursor.execute("INSERT INTO ages VALUES %s " % str(data))



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
	  		
	  		data = (ZipCode, MsaID, MsaName, State)
	  		print(data)
	  		cursor.execute("INSERT INTO geodata VALUES %s " % str(data))



def main():
	add_geo_data()
	add_ftc_data()
	add_age_data()
	add_population_data()
	add_income_data()

	connection.commit()

if __name__ == '__main__':
	main()