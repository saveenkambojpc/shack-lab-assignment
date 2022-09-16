import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://theverge.com"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent,'html.parser')

anchors = soup.find_all('a')
links = set()


for i in anchors:
    if len(i.get('href')) > 25 and not i.img and i.get('class') != None and i.get('href')[0] != 'h' and i.get('href')[1] != 'a':
        if i.next_sibling and i.next_sibling.a :
            links.add(i)

fields = ['id', 'url', 'headline', 'author', 'date']

data = []

id = 0
for i in links:
    headline = i.string,
    date = i.next_sibling.a.next_sibling.string
    url = 'https://theverge.com/'+i.get('href')
    author = i.next_sibling.a.string
    fdate = datetime.strptime(date+' 2022','%b %d %Y').date().strftime("%Y/%m/%d")
    obj = {}
    obj['headline'] = headline
    obj['url'] = url
    obj['author'] = author
    obj['date'] = fdate
    obj['id'] = id
    

    id = id+1
    data.append(obj)


# CSV File Generation
rows = []
for row in data:
    arr = [row['id'],row['url'],row['headline'][0],row['author'],row['date']]

    rows.append(arr)

# name of csv file 
filename = "headline_records.csv"

# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)


