import requests
from bs4 import BeautifulSoup
import pandas as pd


"""
Scraping script to retrieve data from indeed.
To Implement:
Indeed NZ(Soft Dev) [x]
Indeed AU(Soft Dev) [x]
Combine all into .csv for project [] 
"""

# Extract- NZ Indeed(Software Developer)
def extractnz(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83'}
    urlNZ = f"https://nz.indeed.com/jobs?q=software+developer&l=New+Zealand&vjk=118731a217acab33&start={page}"
    r = requests.get(urlNZ, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    return soup



#Transform
def transformnz(soup):
    divs = soup.find_all('div', class_='cardOutline')
    for item in divs:
        title = item.find('a').text.strip()
        try:
            company = item.find('span', class_='companyName').text.strip()
        except AttributeError:
            company = 'N/A'
        try:
            location = item.find('div', class_='companyLocation').text.strip().replace('\n', '')
        except AttributeError:
            locaton = 'N/A'
        try:
            summary = item.find('div', class_='job-snippet').text.strip()
        except AttributeError:
            summary = 'N/A'
        try:
            posted = item.find('span', class_='date').text.strip()
        except AttributeError:
            posted = 'N/A'
        job = {
            'Title' : title,
            'Company' : company,
            'Location' : location,
            'Summary' : summary,
            'Posted' : posted
        }
        jobListnz.append(job)
    return

jobListnz = []

for i in range(0, 60, 10):
    print(f'Getting Page, {i}')
    c = extractnz(0)
    transformnz(c)

dfnz = pd.DataFrame(jobListnz)

print(dfnz.head())

dfnz.to_csv('NZSD.csv') #NZ Software Dev Jobs

#Extract - Au Indeed(Software Developer)
def extractau(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83'}
    urlAU = f"https://au.indeed.com/jobs?q=Software%20Developer&start={page}&vjk=7fbac8aeaba92384"
    r = requests.get(urlAU, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transformau(soup):
    divs = soup.find_all('div', class_='cardOutline')
    for item in divs:
        title = item.find('a').text.strip()
        try:
            company = item.find('span', class_='companyName').text.strip()
        except AttributeError:
            company = 'N/A'
        try:
            location = item.find('div', class_='companyLocation').text.strip().replace('\n', '')
        except AttributeError:
            locaton = 'N/A'
        try:
            summary = item.find('div', class_='job-snippet').text.strip()
        except AttributeError:
            summary = 'N/A'
        try:
            posted = item.find('span', class_='date').text.strip()
        except AttributeError:
            posted = 'N/A'
        
        job = {
            'Title' : title,
            'Company' : company,
            'Location' : location,
            'Summary' : summary,
            'Posted' : posted
        }
        jobListau.append(job)
    return

jobListau = []

for i in range(0, 60, 10):
    print(f'Getting Page, {i}')
    c = extractau(0)
    transformau(c)

dfau = pd.DataFrame(jobListau)

print(dfau.head())

dfau.to_csv('AUSD.csv')

