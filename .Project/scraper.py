import requests
from bs4 import BeautifulSoup
import pandas as pd

# Extract
def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    urlNZ = f"https://nz.indeed.com/jobs?q=software%20developer&l=New%20Zealand&vjk=118731a217acab33&start={page}"
    r = requests.get(urlNZ, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup



#Transform
def transform(soup):
    divs = soup.find_all('div', class_='cardOutline')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_='companyName').text.strip()
        location = item.find('div', class_='companyLocation').text.strip().replace('\n', '')
        summary = item.find('div', class_='job-snippet').text.strip()
        
        job = {
            'Title' : title,
            'Company' : company,
            'Location' : location,
            'Summary' : summary
        }
        jobList.append(job)
    return

jobList = []

for i in range(0, 40, 10):
    print(f'Getting Page, {i}')
    c = extract(0)
    transform(c)

df = pd.DataFrame(jobList)

print(df.head())

df.to_csv('jobs.csv')