# Scrape college graduates percenteage from zipatlas
import sys
import bs4
import requests
import csv
import time

BASE_URL = "http://zipatlas.com/us/zip-code-comparison/percentage-college-graduates.htm"
csv_file = open("college_data.csv", "w")
data_writer = csv.writer(csv_file,delimiter=',')

for i in range(1, 318):

	if i == 1:
		new_url = BASE_URL
		r = requests.get(new_url)
	else:
		new = str(i)+".htm"
		new_url = BASE_URL.replace("htm",new)
		r = requests.get(new_url)

	if r.status_code == 200:
		print("new_page")
		page_content = r.content

		data = bs4.BeautifulSoup(page_content, "html.parser")
		zip_data = data.find_all("td", { "class" : "report_data"})

		for x in range(0,700,7):
			result_arr = []
			new_data = (zip_data[x:x+7])
			
			for j in new_data:
				result_arr.append(j.text.replace(",", "."))
			data_writer.writerow(result_arr)
		time.sleep(5)
		print(new_url)
