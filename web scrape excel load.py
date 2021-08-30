from bs4 import BeautifulSoup as bsoup
import requests
from csv import writer

url = #add a web page here and edit the html class accordingly.
html_text = requests.get(url).text
soup = bsoup(html_text, 'lxml')
projects = soup.find_all('article', class_="css-1nr7r9e")

with open('assets.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Property_Name', 'Address', 'Property_Value', 'Property_Specification']
    thewriter.writerow(header)

    for project in projects:
        project_name = project.find('h3', class_="css-zekqfr").text
        project_price = project.find('div', class_="css-18rodr0").text
        project_address = project.find('a', class_="css-16drx2b").text
        project_spec = project.find('div', class_="css-1ty8tu4").text
        info = [project_name, project_address, project_price, project_spec]
        thewriter.writerow(info)


