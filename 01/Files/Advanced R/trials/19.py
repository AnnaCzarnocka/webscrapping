import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = 'https://nofluffjobs.com/pl/?lang=en&gclid=CjwKCAjwscGjBhAXEiwAswQqNB0HL4nZul0aq27jiZv4ZUlZ0UjUWfTdQfZMP_TCwygRpwYXGTDhtBoCIQcQAvD_BwE&criteria=keyword%3D%27senior%20software%20engineer%27%20jobLanguage%3Den&page=1'
response = requests.get(url)

# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <a> elements with the job links
job_links = soup.find_all('a', {'_ngcontent-serverapp-c304': '', 'nfj-postings-item': '', '_nghost-serverapp-c309': ''})

# Extract the href attribute from each job link and print it
for link in job_links:
    job_link = link.get('href')
    print(job_link)
