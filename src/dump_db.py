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
		CREATE TABLE ftc_data(
			Organization TEXT, 
        	CustomerZip NUMERIC, 
        	FraudZip NUMERIC, 
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

	  		cursor.execute("INSERT INTO ftc_data VALUES %s " % str(data))



def add_population_data():
	print("aa")

def main():
	add_ftc_data()
	connection.commit()


if __name__ == '__main__':
	main()