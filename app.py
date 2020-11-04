from bs4 import BeautifulSoup
import requests
import csv

## Create CSV file
csv_file = open('events.csv', 'w')

## Create A Writer Object to write to file
csv_writer = csv.writer(csv_file)

## Create Table Headings
csv_writer.writerow(["Name", "Start Date", "End Date", "Location", "Address", "Link"])

#Create A For Loop to Iterate through pages
for page in range(1, 4):
	## Get Url
	url = f"http://aixr.org/events-listing/list/page/{page}/"

	## Convert Html to String
	source = requests.get(url).text
	
	## Convert String to Soup Object
	soup = BeautifulSoup(source, 'lxml')

	## Iterate through All Events per page		
	for event in soup.find_all('div', class_='tribe-events-calendar-list__event-wrapper tribe-common-g-col'):

		## Get Link of Event
		link = event.find('a')['href']
		# print(link)
		
		## Get Start Date
		start = event.find('span', class_='tribe-event-date-start').text
		# print(start)
		
		## If There is no End Date return None
		try:
			end = event.find('span', class_='tribe-event-date-end').text		
		except:
			end = None
		# print(end)

		## If Event has No Name Return None
		try:
			name = event.find('a')['title']
		except:
			name = None
		# print(name)

		# If Event has no location return None
		try:
			location = event.find('span', class_='tribe-events-calendar-list__event-venue-title tribe-common-b2--bold').text
		except:
			location = None
		# print(location)

		# If Event has no address return None
		try:
			address = event.find('span', class_='tribe-events-calendar-list__event-venue-address').text
		except:
			address = None
		# print(address)

		## Add Data into SpreadSheet
		csv_writer.writerow([name, start, end, location, address, link])

## Close CSV File
csv_file.close()

## Verify Process is Completed
print("Extracted")	

