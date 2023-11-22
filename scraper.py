from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = 'https://careers.ibm.com/job/19448034/entry-level-devops-developer-markham-ca/?codes=SN_LinkedIn&Codes=SN_LinkedIn'

url2 = 'https://jobs.rogers.com/job/Mississauga-Sales-Associate-ON/1100462100/?feedId=23200&utm_source=LinkedInJobPostings&utm_campaign=Rogers_PremiumFeeds'



def extract_data(url):

    page = urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    return soup.get_text(), html, soup

def find_title(text):

    text, html, soup = extract_data(url2)
    title = ''
    for i in soup.title.get_text():
        if soup.title:
            title += str(i)

    
    # re.sub('(<!--.*?-->|<[^>]*>)', '', title)

    # para = soup.find_all('p')
    # text = [soup.get_text(strip = True) for i in title]
    return title

title = find_title(url2)



print(title)